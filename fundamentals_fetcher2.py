import pandas as pd
import yfinance as yf
from datetime import datetime
import os
import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# ===== 設定 =====
BATCH_SIZE = 50
MAX_WORKERS = 5
RETRY_MAX = 3
BATCH_SLEEP = 5

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ===== ユーティリティ =====

def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


# ===== データ取得 =====

def fetch_one(symbol):
    """単一銘柄取得"""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        data = {
            'Symbol': symbol,
            'Date': datetime.now().strftime('%Y-%m-%d'),
            'PER': info.get('trailingPE', None),
            'ROE': info.get('returnOnEquity', None),
            'Company_Name': info.get('longName', None),
        }

        return data

    except Exception as e:
        logger.warning(f"{symbol} fetch error: {e}")
        return None


def validate(data):
    """データ検証"""
    if data is None:
        return False

    # PER/ROEどちらもNoneなら失敗扱い
    if data['PER'] is None and data['ROE'] is None:
        return False

    return True


def fetch_with_retry(symbol):
    """リトライ付き取得"""
    for attempt in range(RETRY_MAX):
        data = fetch_one(symbol)

        if validate(data):
            return data

        wait = 2 ** attempt
        logger.info(f"{symbol} retry {attempt+1} after {wait}s")
        time.sleep(wait)

    return None


# ===== メイン処理 =====

def fetch_batch(batch):
    """1バッチ並列処理"""
    results = []
    failed = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch_with_retry, s): s for s in batch}

        for future in as_completed(futures):
            symbol = futures[future]

            try:
                data = future.result()
                if data:
                    results.append(data)
                else:
                    failed.append(symbol)

            except Exception as e:
                logger.error(f"{symbol} future error: {e}")
                failed.append(symbol)

    return results, failed


def fetch_all(symbols):
    """全体処理"""
    all_results = []
    failed_symbols = []

    batches = list(chunk_list(symbols, BATCH_SIZE))

    logger.info(f"Total batches: {len(batches)}")

    for i, batch in enumerate(batches):
        logger.info(f"Processing batch {i+1}/{len(batches)}")

        results, failed = fetch_batch(batch)

        all_results.extend(results)
        failed_symbols.extend(failed)

        logger.info(f"Batch done: success={len(results)} failed={len(failed)}")

        # バッチ間スリープ
        time.sleep(BATCH_SLEEP)

    return all_results, failed_symbols


def retry_failed(symbols):
    """失敗銘柄の再処理"""
    if not symbols:
        return []

    logger.info(f"Retrying {len(symbols)} failed symbols...")

    results = []
    for s in symbols:
        data = fetch_with_retry(s)
        if data:
            results.append(data)

    return results


# ===== 入出力 =====

def load_symbols(csv_path):
    df = pd.read_csv(csv_path)
    return df.iloc[:, 0].astype(str).tolist()


def save_data(data_list, output_path):
    df = pd.DataFrame(data_list)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return df


# ===== メイン =====

def main():
    symbols = load_symbols('data_store/symbols.csv')

    logger.info(f"Total symbols: {len(symbols)}")

    # ① 本処理
    results, failed = fetch_all(symbols)

    # ② 失敗再処理
    retry_results = retry_failed(failed)

    # 統合
    all_data = results + retry_results

    df = save_data(all_data, 'data_store/fundamentals/raw.csv')

    logger.info(f"Final records: {len(df)}")
    logger.info(f"Remaining failed: {len(symbols) - len(df)}")


if __name__ == '__main__':
    main()
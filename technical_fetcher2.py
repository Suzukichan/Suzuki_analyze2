import pandas as pd
import yfinance as yf
import os
import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# ===== 設定 =====
BATCH_SIZE = 50
MAX_WORKERS = 5
RETRY_MAX = 3
BATCH_SLEEP = 5
PERIOD = "60d"

# ===== ログ =====
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

def fetch_one(symbol_info):
    """1銘柄取得"""
    code = symbol_info["Code"]
    stock_tse_code = f"{code}.T"

    try:
        df = yf.download(stock_tse_code, period=PERIOD, interval="1d", progress=False)

        if df.empty:
            return None

        records = []
        for date, row in df.iterrows():
            records.append({
                'Code': code,
                'Name': symbol_info["Name"],
                'Market': symbol_info["Market"],
                'Sector': symbol_info["Sector"],
                'Date': date.strftime('%Y-%m-%d'),
                'Close': row['Close'],
                'Volume': row['Volume']
            })

        return records

    except Exception as e:
        logger.warning(f"{stock_tse_code} fetch error: {e}")
        return None


def validate(records):
    """データ検証"""
    if records is None or len(records) == 0:
        return False

    # 最低日数チェック（約60営業日）
    if len(records) < 40:
        return False

    # 欠損チェック
    for r in records:
        if pd.isna(r["Close"]) or pd.isna(r["Volume"]):
            return False

    return True


def fetch_with_retry(symbol_info):
    """リトライ付き取得"""
    for attempt in range(RETRY_MAX):
        data = fetch_one(symbol_info)

        if validate(data):
            return data

        wait = 2 ** attempt
        logger.info(f"{symbol_info['Code']} retry {attempt+1} after {wait}s")
        time.sleep(wait)

    return None

# ===== バッチ処理 =====

def fetch_batch(batch):
    results = []
    failed = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch_with_retry, s): s for s in batch}

        for future in as_completed(futures):
            symbol_info = futures[future]
            code = symbol_info["Code"]

            try:
                data = future.result()
                if data:
                    results.extend(data)
                else:
                    failed.append(symbol_info)

            except Exception as e:
                logger.error(f"{code} future error: {e}")
                failed.append(symbol_info)

    return results, failed


def fetch_all(symbols_info):
    all_results = []
    failed_symbols = []

    batches = list(chunk_list(symbols_info, BATCH_SIZE))
    logger.info(f"Total batches: {len(batches)}")

    for i, batch in enumerate(batches):
        logger.info(f"Processing batch {i+1}/{len(batches)}")

        results, failed = fetch_batch(batch)

        all_results.extend(results)
        failed_symbols.extend(failed)

        logger.info(f"Batch done: success={len(results)} rows, failed={len(failed)} symbols")

        time.sleep(BATCH_SLEEP)

    return all_results, failed_symbols


def retry_failed(symbols_info):
    if not symbols_info:
        return []

    logger.info(f"Retrying {len(symbols_info)} failed symbols...")

    results = []
    for s in symbols_info:
        data = fetch_with_retry(s)
        if data:
            results.extend(data)

    return results

# ===== メイン =====

def main():
    # 読み込み
    df_symbols = pd.read_csv('data_store/symbols.csv')

    symbols_info = df_symbols.to_dict(orient='records')

    logger.info(f"Total symbols: {len(symbols_info)}")

    # 本処理
    results, failed = fetch_all(symbols_info)

    # 再処理
    retry_results = retry_failed(failed)

    # 統合
    all_data = results + retry_results

    result_df = pd.DataFrame(all_data)

    # 保存
    os.makedirs('data_store/technical', exist_ok=True)
    result_df.to_csv('data_store/technical/raw.csv', index=False, encoding='utf-8')

    logger.info(f"Final rows: {len(result_df)}")
    logger.info(f"Remaining failed symbols: {len(failed)}")


if __name__ == "__main__":
    main()
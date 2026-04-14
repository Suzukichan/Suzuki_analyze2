import pandas as pd
import yfinance as yf
from datetime import datetime
import os
import time
import logging

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_symbols(csv_path='data_store/symbols.csv'):
    """
    CSVファイルから銘柄コードを読み込む
    
    Parameters:
    -----------
    csv_path : str
        symbols.csvへのパス
    
    Returns:
    --------
    list : 銘柄コードのリスト
    """
    try:
        df = pd.read_csv(csv_path)
        # 銘柄コードが含まれるカラムを想定（例:"Symbol"や最初のカラム）
        if 'Symbol' in df.columns:
            symbols = df['Symbol'].tolist()
        else:
            symbols = df.iloc[:, 0].tolist()
        
        logger.info(f"Successfully loaded {len(symbols)} symbols from {csv_path}")
        return symbols
    except FileNotFoundError:
        logger.error(f"File not found: {csv_path}")
        return []
    except Exception as e:
        logger.error(f"Error loading symbols: {e}")
        return []

def fetch_fundamental_data(symbols, output_path='data_store/fundamentals/raw.csv'):
    """
    yfinanceを使用してファンダメンタルデータを取得
    
    Parameters:
    -----------
    symbols : list
        銘柄コードのリスト
    output_path : str
        出力先CSVファイルのパス
    
    Returns:
    --------
    pd.DataFrame : 取得したファンダメンタルデータ
    """
    data_list = []
    
    for symbol in symbols:
        try:
            logger.info(f"Fetching data for {symbol}...")
            
            # yfinanceでティッカーデータを取得
            ticker = yf.Ticker(symbol)
            
            # 情報を取得
            info = ticker.info
            
            # ファンダメンタルデータを抽出
            fundamental_data = {
                'Symbol': symbol,
                'Date': datetime.now().strftime('%Y-%m-%d'),
                'PER': info.get('trailingPE', None),  # Trailing P/E Ratio
                'ROE': info.get('returnOnEquity', None),  # Return on Equity
                'Company_Name': info.get('longName', None),
            }
            
            data_list.append(fundamental_data)
            logger.info(f"Successfully fetched data for {symbol}")
            
        except Exception as e:
            logger.warning(f"Error fetching data for {symbol}: {e}")
            # エラーの場合でもNaNで記録
            data_list.append({
                'Symbol': symbol,
                'Date': datetime.now().strftime('%Y-%m-%d'),
                'PER': None,
                'ROE': None,
                'Company_Name': None,
            })
            
        time.sleep(0.3)
    
    # DataFrameに変換
    df = pd.DataFrame(data_list)
    
    # 出力ディレクトリが存在しない場合は作成
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    
    # CSVファイルに保存
    df.to_csv(output_path, index=False, encoding='utf-8')
    logger.info(f"Data saved to {output_path}")
    
    return df

def main():
    """メイン処理"""
    logger.info("Starting fundamental data fetcher...")
    
    # ���柄コードを読み込み
    symbols = load_symbols('data_store/symbols.csv')
    
    if not symbols:
        logger.error("No symbols to process. Exiting.")
        return
    
    # ファンダメンタルデータを取得して保存
    df = fetch_fundamental_data(symbols, 'data_store/fundamentals/raw.csv')
    
    # 取得結果を表示
    logger.info(f"Total records: {len(df)}")
    logger.info(f"Records with PER data: {df['PER'].notna().sum()}")
    logger.info(f"Records with ROE data: {df['ROE'].notna().sum()}")
    
    logger.info("Fundamental data fetcher completed!")


if __name__ == '__main__':
    main()
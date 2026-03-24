import pandas as pd
import yfinance as yf
from tqdm import tqdm
import os

def fetch_fundamentals(progress_callback=None):
    """
    Fetch fundamental data (PER, PBR, ROE) for Japanese stocks
    Read symbols from data_store/symbols.csv
    Save results to data_store/fundamentals/raw.csv
    """
    # Create output directory if it doesn't exist
    os.makedirs('data_store/fundamentals', exist_ok=True)
    
    # Read symbols from CSV
    symbols_df = pd.read_csv('data_store/symbols.csv', sep='\t')
    results = []
    total = len(symbols_df)
    
    # Iterate through each stock code
    for idx, row in tqdm(symbols_df.iterrows(), total=total, desc="Fetching fundamentals"):
        if progress_callback:
            progress_callback(idx, total)
        code = str(row['Code'])
        name = row['Name']
        
        # Convert code to Tokyo Stock Exchange format (e.g., 1301 -> 1301.T)
        symbol = f"{code}.T"
        
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            
            # Extract fundamental metrics
            per = info.get('trailingPE')  # Price-to-Earnings Ratio
            pbr = info.get('priceToBook')  # Price-to-Book Ratio
            roe = info.get('returnOnEquity')  # Return on Equity
            
            results.append({
                'Code': code,
                'Name': name,
                'PER': per,
                'PBR': pbr,
                'ROE': roe
            })
        except Exception as e:
            print(f'Error fetching data for {code} ({name}): {e}')
            results.append({
                'Code': code,
                'Name': name,
                'PER': None,
                'PBR': None,
                'ROE': None
            })
    
    if progress_callback:
        progress_callback(total, total)

    # Save results to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv('data_store/fundamentals/raw.csv', index=False)
    print(f"\nSaved {len(results)} records to data_store/fundamentals/raw.csv")

if __name__ == '__main__':
    fetch_fundamentals()

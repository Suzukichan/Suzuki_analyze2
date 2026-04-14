import pandas as pd
import yfinance as yf
from tqdm import tqdm
import os
import time

# Step 1: Read symbols from data_store/symbols.csv
symbols_df = pd.read_csv('data_store/symbols.csv')

# Prepare a list to store data
data = []

# Step 2: Fetch 60 days of historical price data for each stock
for index, row in tqdm(symbols_df.iterrows(), total=symbols_df.shape[0]):
    code = row['Code']
    name = row['Name']
    market = row['Market']
    sector = row['Sector']

    # Convert code to Tokyo Stock Exchange format
    stock_tse_code = f'{code}.T'

    try:
        # Step 3: Fetch historical data
        stock_data = yf.download(stock_tse_code, period='60d', interval='1d')
        for date, row in stock_data.iterrows():
            # Step 4: Append results
            data.append({
                'Code': code,
                'Name': name,
                'Market': market,
                'Sector': sector,
                'Date': date.strftime('%Y-%m-%d'),
                'Close': row['Close'],
                'Volume': row['Volume']
            })
    except Exception as e:
        print(f"Error fetching data for {stock_tse_code}: {str(e)}")
        
    time.sleep(0.3)

# Step 5: Save results to data_store/technical/raw.csv
result_df = pd.DataFrame(data)

# Ensure the directory exists
os.makedirs('data_store/technical', exist_ok=True)

result_df.to_csv('data_store/technical/raw.csv', index=False, encoding='utf-8')

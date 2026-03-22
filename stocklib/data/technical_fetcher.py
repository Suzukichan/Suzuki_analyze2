import pandas as pd
import yfinance as yf
import os
from datetime import datetime, timedelta

def fetch_technical_data():
    """
    Fetch 60 days of technical data (Close, Volume) for Japanese stocks
    Read symbols from data_store/symbols.csv
    Save results to data_store/technical/raw.csv
    """
    # Create output directory if it doesn't exist
    os.makedirs('data_store/technical', exist_ok=True)
    
    # Read symbols from CSV
    symbols_df = pd.read_csv('data_store/symbols.csv')
    all_results = []
    
    # Calculate date range (60 days)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=60)
    
    # Iterate through each stock code
    for idx, row in symbols_df.iterrows():
        code = str(row['Code']).zfill(4)
        name = row['Name']
        market = row['Market']
        sector = row['Sector']
        
        # Convert code to Tokyo Stock Exchange format (e.g., 1301 -> 1301.T)
        symbol = f"{code}.T"
        
        try:
            # Fetch historical data
            stock = yf.Ticker(symbol)
            hist = stock.history(start=start_date, end=end_date)
            
            if len(hist) > 0:
                # Reset index to make Date a column
                hist_reset = hist.reset_index()
                
                # Add Code, Name, Market, Sector columns
                hist_reset['Code'] = code
                hist_reset['Name'] = name
                hist_reset['Market'] = market
                hist_reset['Sector'] = sector
                
                # Rename columns and select required columns
                hist_reset.rename(columns={'Date': 'Date', 'Close': 'Close', 'Volume': 'Volume'}, inplace=True)
                
                # Select and reorder columns
                result_df = hist_reset[['Code', 'Name', 'Market', 'Sector', 'Date', 'Close', 'Volume']]
                
                # Convert Date to string format (YYYY-MM-DD)
                result_df['Date'] = result_df['Date'].dt.strftime('%Y-%m-%d')
                
                all_results.append(result_df)
            else:
                print(f'No data available for {code} ({name})')
                
        except Exception as e:
            print(f'Error fetching technical data for {code} ({name}): {e}')
    
    # Combine all results
    if all_results:
        final_df = pd.concat(all_results, ignore_index=True)
        final_df.to_csv('data_store/technical/raw.csv', index=False)
        print(f"\nSaved {len(final_df)} records to data_store/technical/raw.csv")
    else:
        print("No data was fetched")

if __name__ == '__main__':
    fetch_technical_data()

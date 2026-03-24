import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

def combine_data_to_excel(fundamentals_path='data_store/fundamentals/raw.csv',
                          technical_path='data_store/technical/raw.csv',
                          output_path='data_store/combined/combined.xlsx'):
    """
    ファンダメンタルズデータとテクニカルデータを1つのExcelファイルの別シートに結合する
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # データの読み込み
    try:
        df_fund = pd.read_csv(fundamentals_path)
    except FileNotFoundError:
        df_fund = pd.DataFrame()
        logger.warning(f"File not found: {fundamentals_path}")
        
    try:
        df_tech = pd.read_csv(technical_path)
    except FileNotFoundError:
        df_tech = pd.DataFrame()
        logger.warning(f"File not found: {technical_path}")
        
    # Excelに書き込み
    with pd.ExcelWriter(output_path) as writer:
        if not df_fund.empty:
            df_fund.to_excel(writer, sheet_name='Fundamentals', index=False)
        else:
            pd.DataFrame({'Message': ['No data']}).to_excel(writer, sheet_name='Fundamentals', index=False)
            
        if not df_tech.empty:
            df_tech.to_excel(writer, sheet_name='Technical', index=False)
        else:
            pd.DataFrame({'Message': ['No data']}).to_excel(writer, sheet_name='Technical', index=False)
            
    print(f"Data combined and saved to {output_path}")

import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import pandas as pd
import yfinance as yf
import time

# プロジェクトルートにパスを通す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("シミュレーション")
        self.root.geometry("400x300")

        # パディング用のメインフレーム
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # シミュレーションデータ収集ボタン
        self.btn_collect_data = ttk.Button(main_frame, text="シミュレーションデータ収集", command=self.collect_data)
        self.btn_collect_data.pack(fill=tk.X, pady=10)

        # 戦略編集ボタン
        self.btn_edit_strategy = ttk.Button(main_frame, text="戦略編集", command=self.dummy_action)
        self.btn_edit_strategy.pack(fill=tk.X, pady=10)

        # シミュレーション実行ボタン
        self.btn_run_simulation = ttk.Button(main_frame, text="シミュレーション実行", command=self.dummy_action)
        self.btn_run_simulation.pack(fill=tk.X, pady=10)

        # ステータス表示用ラベル
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.pack(fill=tk.X, pady=5)

        # プログレスバー
        self.progress_bar = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, mode='determinate')
        self.progress_bar.pack(fill=tk.X, pady=5)

    def dummy_action(self):
        """ボタンが押された時のダミー処理"""
        print("機能未実装")

    def collect_data(self):
        """データ収集ボタンが押された時の処理"""
        self.btn_collect_data.config(state=tk.DISABLED)
        self.status_label.config(text="データ収集中...")
        self.progress_bar['value'] = 0
        
        # GUIのフリーズを防ぐため別スレッドで実行
        threading.Thread(target=self._fetch_simulation_data, daemon=True).start()

    def _fetch_simulation_data(self):
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            symbols_path = os.path.join(base_dir, "data_store", "symbols.csv")
            output_path = os.path.join(base_dir, "data_store", "simulation.csv")

            if not os.path.exists(symbols_path):
                self.root.after(0, lambda: messagebox.showerror("エラー", f"{symbols_path}が見つかりません。"))
                return

            # タブ区切りかカンマ区切りか判定して読み込み
            with open(symbols_path, 'r', encoding='utf-8') as f:
                first_line = f.readline()
            sep = '\t' if '\t' in first_line else ','
            df_symbols = pd.read_csv(symbols_path, sep=sep)
            
            if 'Code' not in df_symbols.columns:
                self.root.after(0, lambda: messagebox.showerror("エラー", "symbols.csvにCode列が存在しません。"))
                return
            
            tickers = [f"{str(code)}.T" for code in df_symbols['Code'].astype(str)]
            total_tickers = len(tickers)
            
            # プログレスバーの最大値を設定
            self.root.after(0, lambda: self.progress_bar.config(maximum=total_tickers))
            
            all_data = []
            
            # APIのRate Limit回避とメモリ節約のため、100件ずつのチャンクに分けて処理
            chunk_size = 100
            for i in range(0, len(tickers), chunk_size):
                chunk_tickers = tickers[i:min(i + chunk_size, len(tickers))]
                
                # プログレス非表示でyfinanceからデータ取得
                data = yf.download(chunk_tickers, period="500d", group_by="ticker", progress=False)
                
                if len(chunk_tickers) == 1:
                    ticker = chunk_tickers[0]
                    if not data.empty:
                        df_ticker = data[['Close', 'Volume']].copy()
                        df_ticker['Code'] = ticker.replace('.T', '')
                        df_ticker = df_ticker.reset_index()
                        all_data.append(df_ticker)
                else:
                    for ticker in chunk_tickers:
                        if ticker in data and not data[ticker].empty:
                            df_ticker = data[ticker][['Close', 'Volume']].copy()
                            df_ticker = df_ticker.dropna(subset=['Close', 'Volume'])
                            if not df_ticker.empty:
                                df_ticker['Code'] = ticker.replace('.T', '')
                                df_ticker = df_ticker.reset_index()
                                all_data.append(df_ticker)
                
                # APIリクエスト制限を回避するための待機（以前の要件に合わせて0.3秒）
                time.sleep(0.3)
                
                progress = min(i + chunk_size, len(tickers))
                self.root.after(0, lambda p=progress, t=len(tickers): self._update_progress_ui(p, t))

            if all_data:
                final_df = pd.concat(all_data, ignore_index=True)
                
                # symbols.csvの情報を結合
                df_symbols['Code'] = df_symbols['Code'].astype(str)
                final_df = pd.merge(final_df, df_symbols[['Code', 'Name', 'Market', 'Sector']], on='Code', how='left')
                
                # 日付列の名前とフォーマットを調整
                if 'Datetime' in final_df.columns:
                    final_df.rename(columns={'Datetime': 'Date'}, inplace=True)
                elif 'index' in final_df.columns:
                    final_df.rename(columns={'index': 'Date'}, inplace=True)

                if 'Date' in final_df.columns:
                    final_df['Date'] = pd.to_datetime(final_df['Date']).dt.strftime('%Y-%m-%d')
                
                # 列の並び順を指定に合わせて変更
                columns_order = ['Code', 'Name', 'Market', 'Sector', 'Date', 'Close', 'Volume']
                # 万が一欠落している列があってもエラーにならないようにフィルタリング
                final_cols = [c for c in columns_order if c in final_df.columns]
                final_df = final_df[final_cols]
                
                final_df.to_csv(output_path, index=False, encoding='utf-8')
                self.root.after(0, lambda: messagebox.showinfo("完了", f"シミュレーションデータを保存しました。\n{output_path}"))
            else:
                self.root.after(0, lambda: messagebox.showwarning("警告", "データが取得できませんでした。"))

        except Exception as e:
            self.root.after(0, lambda err=str(e): messagebox.showerror("エラー", f"取得中にエラーが発生しました:\n{err}"))
        finally:
            self.root.after(0, lambda: self.btn_collect_data.config(state=tk.NORMAL))
            self.root.after(0, lambda: self.status_label.config(text=""))
            self.root.after(0, lambda: self.progress_bar.config(value=0))

    def _update_progress_ui(self, progress, total):
        self.status_label.config(text=f"データ収集中... ({progress}/{total})")
        self.progress_bar['value'] = progress

if __name__ == '__main__':
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()

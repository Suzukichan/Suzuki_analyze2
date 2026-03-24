import sys
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stocklib.data.fundamentals_fetcher import fetch_fundamentals
from stocklib.data.technical_fetcher import fetch_technical_data
from stocklib.analysis.combined import combine_data_to_excel

class AdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("管理者用ウインドウ - データ収集・設定")
        self.root.geometry("400x350")
        
        # タイトル
        title_label = tk.Label(root, text="データ管理パネル", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        
        # ボタン群
        self.btn_fund = tk.Button(root, text="ファンダメンタルデータ収集", command=self.run_fundamentals, width=30)
        self.btn_fund.pack(pady=5)
        
        self.btn_tech = tk.Button(root, text="テクニカルデータ収集", command=self.run_technical, width=30)
        self.btn_tech.pack(pady=5)
        
        self.btn_both = tk.Button(root, text="両データ収集（順次実行）", command=self.run_both, width=30)
        self.btn_both.pack(pady=5)
        
        self.btn_combine = tk.Button(root, text="統合データ参照（Excelへ統合）", command=self.run_combine, width=30)
        self.btn_combine.pack(pady=5)
        
        # プログレスバー
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(pady=15, fill=tk.X, padx=30)
        
        # ステータスラベル
        self.status_label = tk.Label(root, text="待機中...")
        self.status_label.pack(pady=5)

    def update_progress(self, current, total):
        if total > 0:
            pct = (current / total) * 100
            self.progress_var.set(pct)
            self.status_label.config(text=f"処理中... {current}/{total} ({pct:.1f}%)")
            self.root.update_idletasks()

    def run_fundamentals(self):
        self._disable_buttons()
        self.status_label.config(text="ファンダメンタルデータ収集中...")
        self.progress_var.set(0)
        
        def task():
            try:
                fetch_fundamentals(progress_callback=self.update_progress)
                self.root.after(0, lambda: messagebox.showinfo("完了", "ファンダメンタルデータの収集が完了しました。"))
            except Exception as e:
                err_msg = str(e)
                self.root.after(0, lambda m=err_msg: messagebox.showerror("エラー", f"失敗しました:\n{m}"))
            finally:
                self.root.after(0, self._enable_buttons)
                
        threading.Thread(target=task, daemon=True).start()

    def run_technical(self):
        self._disable_buttons()
        self.status_label.config(text="テクニカルデータ収集中...")
        self.progress_var.set(0)
        
        def task():
            try:
                fetch_technical_data(progress_callback=self.update_progress)
                self.root.after(0, lambda: messagebox.showinfo("完了", "テクニカルデータの収集が完了しました。"))
            except Exception as e:
                err_msg = str(e)
                self.root.after(0, lambda m=err_msg: messagebox.showerror("エラー", f"失敗しました:\n{m}"))
            finally:
                self.root.after(0, self._enable_buttons)
                
        threading.Thread(target=task, daemon=True).start()

    def run_both(self):
        self._disable_buttons()
        self.status_label.config(text="全データ収集中 (1/2: ファンダメンタル)...")
        self.progress_var.set(0)
        
        def task():
            try:
                fetch_fundamentals(progress_callback=self.update_progress)
                self.root.after(0, lambda: self.status_label.config(text="全データ収集中 (2/2: テクニカル)..."))
                fetch_technical_data(progress_callback=self.update_progress)
                self.root.after(0, lambda: messagebox.showinfo("完了", "両方のデータ収集が完了しました。"))
            except Exception as e:
                err_msg = str(e)
                self.root.after(0, lambda m=err_msg: messagebox.showerror("エラー", f"失敗しました:\n{m}"))
            finally:
                self.root.after(0, self._enable_buttons)
                
        threading.Thread(target=task, daemon=True).start()

    def run_combine(self):
        self._disable_buttons()
        self.status_label.config(text="データをExcelに統合中...")
        self.progress_var.set(0)
        
        def task():
            try:
                combine_data_to_excel()
                self.root.after(0, lambda: messagebox.showinfo("完了", "Excelへの統合が完了しました（data_store/combined/combined.xlsx）。"))
            except Exception as e:
                err_msg = str(e)
                self.root.after(0, lambda m=err_msg: messagebox.showerror("エラー", f"失敗しました:\n{m}"))
            finally:
                self.root.after(0, self._enable_buttons)
                
        threading.Thread(target=task, daemon=True).start()

    def _disable_buttons(self):
        self.btn_fund.config(state=tk.DISABLED)
        self.btn_tech.config(state=tk.DISABLED)
        self.btn_both.config(state=tk.DISABLED)
        self.btn_combine.config(state=tk.DISABLED)

    def _enable_buttons(self):
        self.btn_fund.config(state=tk.NORMAL)
        self.btn_tech.config(state=tk.NORMAL)
        self.btn_both.config(state=tk.NORMAL)
        self.btn_combine.config(state=tk.NORMAL)
        self.status_label.config(text="待機中...")
        self.progress_var.set(0)

def main():
    root = tk.Tk()
    app = AdminApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

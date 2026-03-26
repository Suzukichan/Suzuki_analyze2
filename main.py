import sys
import os
import tkinter as tk
from tkinter import messagebox
import subprocess

class AppLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Suzuki Analyze - スタート画面")
        self.root.geometry("400x400")
        
        # タイトル
        title_label = tk.Label(root, text="Suzuki Analyze ランチャー", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)
        
        # 説明
        desc_label = tk.Label(root, text="起動したい画面（機能）を選択してください", font=("Arial", 10))
        desc_label.pack(pady=10)
        
        # ボタン: 管理者画面
        self.btn_admin = tk.Button(root, text="裏方・管理者画面\n(データ収集・統合・設定管理)", 
                                   command=self.launch_admin, width=35, height=1, bg="#f0f0f0")
        self.btn_admin.pack(pady=10)
        
        # ボタン: 分析画面
        self.btn_analysis = tk.Button(root, text="銘柄分析・スクリーニング画面\n(最新データの可視化と絞り込み)", 
                                      command=self.launch_analysis, width=35, height=4, bg="#e6f2ff")
        self.btn_analysis.pack(pady=10)
        
        # ボタン: シミュレーション画面
        self.btn_sim = tk.Button(root, text="バックテスト・シミュレーション画面\n(条件による過去データの取引検証)", 
                                 command=self.launch_simulation, width=35, height=4, bg="#e6ffe6")
        self.btn_sim.pack(pady=10)

    def launch_script(self, script_path):
        # 現在のスクリプトのディレクトリを基準にパスを解決
        base_dir = os.path.dirname(os.path.abspath(__file__))
        target_path = os.path.join(base_dir, "ui", script_path)
        
        if not os.path.exists(target_path):
            messagebox.showerror("エラー", f"ファイルが見つかりません:\n{target_path}")
            return
            
        try:
            # sys.executable を使って現在のPython環境で実行（別プロセスとして独立起動）
            subprocess.Popen([sys.executable, target_path])
        except Exception as e:
            messagebox.showerror("エラー", f"起動に失敗しました:\n{e}")

    def launch_admin(self):
        self.launch_script("app_admin.py")
        
    def launch_analysis(self):
        self.launch_script("app_analysis.py")
        
    def launch_simulation(self):
        self.launch_script("app_simulation.py")

def main():
    root = tk.Tk()
    app = AppLauncher(root)
    root.mainloop()

if __name__ == '__main__':
    main()

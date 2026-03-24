import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# プロジェクトルートにパスを通す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("銘柄分析・スクリーニング")
        self.root.geometry("600x400")
        
        # タイトル
        title_label = tk.Label(root, text="銘柄分析・スクリーニング", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        
        # ========= セクター分析エリア =========
        sector_frame = tk.LabelFrame(root, text="セクター分析", padx=10, pady=10)
        sector_frame.pack(fill="x", padx=20, pady=10)
        
        # セクター分析ボタン
        self.btn_sector_analysis = tk.Button(sector_frame, text="セクター分析を実行", width=25, command=self.dummy_action)
        self.btn_sector_analysis.pack(pady=5)
        
        # ========= セクター内比較エリア =========
        compare_frame = tk.LabelFrame(root, text="セクター内比較", padx=10, pady=10)
        compare_frame.pack(fill="x", padx=20, pady=10)
        
        # セクター選択ラベル
        sector_label = tk.Label(compare_frame, text="セクターを選択:")
        sector_label.pack(side=tk.LEFT, padx=5)
        
        # セクター選択コンボボックス（東証33業種を内蔵）
        sectors = [
            "水産・農林業", "食料品", "鉱業", "石油・石炭製品", "建設業", 
            "金属製品", "ガラス・土石製品", "繊維製品", "パルプ・紙", "化学", 
            "医薬品", "ゴム製品", "輸送用機器", "鉄鋼", "非鉄金属", 
            "機械", "電気機器", "精密機器", "その他製品", "情報・通信業", 
            "サービス業", "電気・ガス業", "陸運業", "海運業", "空運業", 
            "倉庫・運輸関連業", "卸売業", "小売業", "銀行業", "証券、商品先物取引業", 
            "保険業", "その他金融業", "不動産業"
        ]
        self.sector_combo = ttk.Combobox(compare_frame, values=sectors, state="readonly", width=25)
        self.sector_combo.pack(side=tk.LEFT, padx=5)
        if sectors:
            self.sector_combo.current(0)
            
        # セクター内比較ボタン
        self.btn_sector_compare = tk.Button(compare_frame, text="セクター内比較を実行", command=self.dummy_action)
        self.btn_sector_compare.pack(side=tk.LEFT, padx=10)

        # ========= その他 =========
        # 閉じるボタン
        close_btn = tk.Button(root, text="閉じる", command=self.root.quit, width=15)
        close_btn.pack(pady=30)

    def dummy_action(self):
        # 機能は後で作成するため、プレースホルダーとしてメッセージボックスを表示
        messagebox.showinfo("情報", "この機能は現在開発中です。（後で実装されます）")

def main():
    root = tk.Tk()
    app = AnalysisApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

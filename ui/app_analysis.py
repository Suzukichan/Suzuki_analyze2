import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import numpy as np

# プロジェクトルートにパスを通す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("銘柄分析・スクリーニング")
        self.root.geometry("1000x750")
        
        # タイトル
        title_label = tk.Label(root, text="銘柄分析・スクリーニング", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        
        # ========= セクター分析エリア =========
        sector_frame = tk.LabelFrame(root, text="セクター分析", padx=10, pady=10)
        sector_frame.pack(fill="x", padx=20, pady=5)
        
        # セクター分析ボタン
        self.btn_sector_analysis = tk.Button(sector_frame, text="セクター分析を実行", width=25, command=self.run_sector_analysis)
        self.btn_sector_analysis.pack(pady=5)
        
        # セクター分析表示用Treeview
        columns_sec = ("Sector", "Mom5_Avg", "Mom5_Rel", "Mom10_Avg", "Mom10_Rel", "VolRatio_Avg", "VolRatio_Rel")
        self.tree_sector = ttk.Treeview(sector_frame, columns=columns_sec, show="headings", height=8)
        
        self.tree_sector.heading("Sector", text="セクター名")
        self.tree_sector.heading("Mom5_Avg", text="5日モメンタム平均")
        self.tree_sector.heading("Mom5_Rel", text="5日モメンタム相対強度")
        self.tree_sector.heading("Mom10_Avg", text="10日モメンタム平均")
        self.tree_sector.heading("Mom10_Rel", text="10日モメンタム相対強度")
        self.tree_sector.heading("VolRatio_Avg", text="5日出来高変化率")
        self.tree_sector.heading("VolRatio_Rel", text="出来高変化率相対強度")
        
        for col in columns_sec:
            self.tree_sector.column(col, width=130, anchor=tk.E)
        self.tree_sector.column("Sector", width=150, anchor=tk.W)
        self.tree_sector.pack(fill="x", pady=5)
        
        # ========= セクター内比較エリア =========
        compare_frame = tk.LabelFrame(root, text="セクター内比較", padx=10, pady=10)
        compare_frame.pack(fill="both", expand=True, padx=20, pady=5)
        
        # 操作用フレーム
        control_frame = tk.Frame(compare_frame)
        control_frame.pack(fill="x", pady=5)
        
        sector_label = tk.Label(control_frame, text="セクターを選択:")
        sector_label.pack(side=tk.LEFT, padx=5)
        
        # セクター選択コンボボックス
        sectors = [
            "水産・農林業", "食料品", "鉱業", "石油・石炭製品", "建設業", 
            "金属製品", "ガラス・土石製品", "繊維製品", "パルプ・紙", "化学", 
            "医薬品", "ゴム製品", "輸送用機器", "鉄鋼", "非鉄金属", 
            "機械", "電気機器", "精密機器", "その他製品", "情報・通信業", 
            "サービス業", "電気・ガス業", "陸運業", "海運業", "空運業", 
            "倉庫・運輸関連業", "卸売業", "小売業", "銀行業", "証券、商品先物取引業", 
            "保険業", "その他金融業", "不動産業"
        ]
        self.sector_combo = ttk.Combobox(control_frame, values=sectors, state="readonly", width=25)
        self.sector_combo.pack(side=tk.LEFT, padx=5)
        if sectors:
            self.sector_combo.current(0)
            
        self.btn_sector_compare = tk.Button(control_frame, text="セクター内比較を実行", command=self.run_sector_compare)
        self.btn_sector_compare.pack(side=tk.LEFT, padx=10)
        
        # セクター内比較表示用Treeview
        columns_comp = ("Code", "Name", "Mom5", "Mom10", "VolRatio")
        self.tree_compare = ttk.Treeview(compare_frame, columns=columns_comp, show="headings", height=8)
        
        self.tree_compare.heading("Code", text="コード")
        self.tree_compare.heading("Name", text="銘柄名")
        self.tree_compare.heading("Mom5", text="5日モメンタム")
        self.tree_compare.heading("Mom10", text="10日モメンタム")
        self.tree_compare.heading("VolRatio", text="5日出来高変化率")
        
        for col in columns_comp:
            self.tree_compare.column(col, width=120, anchor=tk.E)
        self.tree_compare.column("Code", width=80, anchor=tk.CENTER)
        self.tree_compare.column("Name", width=200, anchor=tk.W)
        self.tree_compare.pack(fill="both", expand=True, pady=5)

        # ========= その他 =========
        close_btn = tk.Button(root, text="閉じる", command=self.root.quit, width=15)
        close_btn.pack(pady=10)

    def compute_all_indicators(self):
        """全ての銘柄について指標を計算する"""
        try:
            df = pd.read_csv('data_store/technical/raw.csv', dtype={'Code': str})
        except Exception as e:
            messagebox.showerror("エラー", f"データの読み込みに失敗しました:\n{e}\n\n※事前に管理者画面からデータ収集を実行してください。")
            return None
            
        # 前処理
        df['Date'] = pd.to_datetime(df['Date'])
        # 銘柄ごと、日付の古い順に並び替え
        df = df.sort_values(by=['Code', 'Date'])
        
        results = []
        grouped = df.groupby('Code')
        
        for code, group in grouped:
            if len(group) < 10:
                continue # 最小限の日数がない場合はスキップ
                
            closes = group['Close'].values
            vols = group['Volume'].values
            
            # ① 5日間回帰モメンタム
            y5 = closes[-5:]
            x5 = np.arange(5)
            mom5 = np.polyfit(x5, y5, 1)[0]
            
            # 10日間回帰モメンタム
            y10 = closes[-10:]
            x10 = np.arange(10)
            mom10 = np.polyfit(x10, y10, 1)[0]
            
            # 5日間出来高変化率 (直近出来高 / 5日間平均出来高)
            vol_last = vols[-1]
            vol_avg5 = vols[-5:].mean()
            vol_ratio = vol_last / vol_avg5 if vol_avg5 > 0 else np.nan
            
            sector = group['Sector'].iloc[-1]
            name = group['Name'].iloc[-1]
            
            results.append({
                'Code': code,
                'Name': name,
                'Sector': sector,
                'Mom5': mom5,
                'Mom10': mom10,
                'VolRatio': vol_ratio
            })
            
        return pd.DataFrame(results)

    def run_sector_analysis(self):
        res_df = self.compute_all_indicators()
        if res_df is None or res_df.empty:
            return
            
        # 既存内容のクリア
        for row in self.tree_sector.get_children():
            self.tree_sector.delete(row)
            
        # ② セクターごとの平均値を集計
        sector_avg = res_df.groupby('Sector')[['Mom5', 'Mom10', 'VolRatio']].mean()
        
        # 相対強度の計算とTreeviewへの挿入
        if '市場全体' in sector_avg.index:
            nikkei_row = sector_avg.loc['市場全体']
            
            for sector, row in sector_avg.iterrows():
                if sector == '市場全体': continue
                # 日経平均との比率(相対強度)
                rel_mom5 = row['Mom5'] / nikkei_row['Mom5'] if nikkei_row['Mom5'] != 0 else np.nan
                rel_mom10 = row['Mom10'] / nikkei_row['Mom10'] if nikkei_row['Mom10'] != 0 else np.nan
                rel_vol = row['VolRatio'] / nikkei_row['VolRatio'] if nikkei_row['VolRatio'] != 0 else np.nan
                
                # ③ 表で表示
                self.tree_sector.insert('', 'end', values=(
                    sector,
                    f"{row['Mom5']:.3f}", f"{rel_mom5:.3f}",
                    f"{row['Mom10']:.3f}", f"{rel_mom10:.3f}",
                    f"{row['VolRatio']:.3f}", f"{rel_vol:.3f}"
                ))
        else:
            # 日経平均データが取得不可の場合（異常系）
            for sector, row in sector_avg.iterrows():
                self.tree_sector.insert('', 'end', values=(
                    sector,
                    f"{row['Mom5']:.3f}", "N/A",
                    f"{row['Mom10']:.3f}", "N/A",
                    f"{row['VolRatio']:.3f}", "N/A"
                ))
                
        # メッセージボックスは邪魔にならないよう表示しないか、シンプルに表示
        # messagebox.showinfo("完了", "セクター分析の計算が完了しました。")

    def run_sector_compare(self):
        target_sector = self.sector_combo.get()
        if not target_sector:
            messagebox.showwarning("警告", "セクターを選択してください。")
            return
            
        res_df = self.compute_all_indicators()
        if res_df is None or res_df.empty:
            return
            
        filtered = res_df[res_df['Sector'] == target_sector]
        
        # 既存内容のクリア
        for row in self.tree_compare.get_children():
            self.tree_compare.delete(row)
            
        if filtered.empty:
            messagebox.showinfo("情報", f"「{target_sector}」のデータが見つかりません。")
            return
            
        # 例として5日モメンタム順（降順）などでソート
        filtered = filtered.sort_values(by='Mom5', ascending=False)
        
        for _, row in filtered.iterrows():
            self.tree_compare.insert('', 'end', values=(
                row['Code'],
                row['Name'],
                f"{row['Mom5']:.3f}",
                f"{row['Mom10']:.3f}",
                f"{row['VolRatio']:.3f}"
            ))

def main():
    root = tk.Tk()
    app = AnalysisApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

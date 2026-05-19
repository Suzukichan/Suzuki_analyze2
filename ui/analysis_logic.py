import pandas as pd
import numpy as np
import os

def compute_all_indicators(technical_csv_path="data_store/technical/raw.csv",
                           fundamentals_csv_path="data_store/fundamentals/raw.csv"):
    """全ての銘柄について指標を計算する"""
    try:
        df = pd.read_csv(technical_csv_path, dtype={"Code": str})
    except Exception as e:
        raise RuntimeError(f"テクニカルデータの読み込みに失敗しました:\n{e}\n\n※事前に管理者画面からデータ収集を実行してください。")

    try:
        fund_df = pd.read_csv(fundamentals_csv_path, dtype={"Code": str})
    except Exception as e:
        # ファンダメンタルズデータがない場合は空のDataFrameを作成
        fund_df = pd.DataFrame(columns=["Code", "Name", "PER", "PBR", "ROE"])

    # 前処理
    df["Date"] = pd.to_datetime(df["Date"])
    # 銘柄ごと、日付の古い順に並び替え
    df = df.sort_values(by=["Code", "Date"])

    results = []
    grouped = df.groupby("Code")

    for code, group in grouped:
        if len(group) < 10:
            continue  # 最小限の日数がない場合はスキップ

        closes = group["Close"].values
        vols = group["Volume"].values

        # ① 5日間回帰モメンタム（%ベース）
        y5 = closes[-5:]
        x5 = np.arange(5)
        slope5 = np.polyfit(x5, y5, 1)[0]
        mom5 = (slope5 / y5.mean()) * 100 if y5.mean() != 0 else 0

        # 10日間回帰モメンタム（%ベース）
        y10 = closes[-10:]
        x10 = np.arange(10)
        slope10 = np.polyfit(x10, y10, 1)[0]
        mom10 = (slope10 / y10.mean()) * 100 if y10.mean() != 0 else 0

        # 5日間出来高変化率 (直近出来高 / 5日間平均出来高)
        vol_last = vols[-1]
        vol_avg5 = vols[-5:].mean()
        vol_ratio = vol_last / vol_avg5 if vol_avg5 > 0 else np.nan

        sector = group["Sector"].iloc[-1]
        name = group["Name"].iloc[-1]

        results.append(
            {
                "Code": code,
                "Name": name,
                "Sector": sector,
                "Mom5": mom5,
                "Mom10": mom10,
                "VolRatio": vol_ratio,
            }
        )

    res_df = pd.DataFrame(results)

    if not res_df.empty and not fund_df.empty:
        # Code列の型を文字列に統一
        fund_df["Code"] = fund_df["Code"].astype(str)
        # PER, PBR, ROEを結合
        res_df = pd.merge(res_df, fund_df[["Code", "PER", "PBR", "ROE"]], on="Code", how="left")
    else:
        res_df["PER"] = np.nan
        res_df["PBR"] = np.nan
        res_df["ROE"] = np.nan

    return res_df

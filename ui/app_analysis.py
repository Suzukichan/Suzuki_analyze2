import sys
import os

# プロジェクトルートにパスを通す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# TODO: StreamlitやDash等を使用して、
# 1. 計算済みの分析データの表示
# 2. screenerを用いた銘柄のフィルタリング（PER, ROE設定等）
# を行うフロントエンドUIをここに実装します。

if __name__ == '__main__':
    print("Starting Analysis & Screening UI...")
    # 例: os.system("streamlit run ui/app_analysis.py")

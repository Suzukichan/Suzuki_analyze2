import sys
import os

# プロジェクトルートにパスを通す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# TODO: StreamlitやDash等を使用して、
# 1. 過去データに対する売買条件の指定とバックテスト実行
# 2. 複数の条件セットでのシミュレーション結果（勝率・損益推移グラフなど）の比較
# を行うシミュレーションUIをここに実装します。

if __name__ == '__main__':
    print("Starting Simulation & Backtest UI...")

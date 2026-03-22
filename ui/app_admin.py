import sys
import os

# プロジェクトルートにパスを通す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# TODO: StreamlitやDash等を使用して、
# 1. fundamentals_fetcher や technical_fetcher の手動実行ボタン（パイプラインの起動）
# 2. ディレクトリやデータ保存先、あるいはシステム全体の設定（config）の管理画面
# を行う裏方（バックエンド管理）UIをここに実装します。

if __name__ == '__main__':
    print("Starting Admin Data Collection UI...")

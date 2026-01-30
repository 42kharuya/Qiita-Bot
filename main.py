import requests
import json
import os  # これを追加

# 直接URLを書かずに、環境変数から読み込む
# "DISCORD_WEBHOOK" はGitHubのSecretsで設定した名前と一致させます
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

def main():
    # URLが取得できていない場合のチェック
    if not DISCORD_WEBHOOK_URL:
        print("Error: DISCORD_WEBHOOK is not set.")
        return

    # --- 以下、前のコードと同じ ---
    RSS_URL = "https://qiita.com/api/v2/items?page=1&per_page=5"
    response = requests.get(RSS_URL)
    articles = response.json()
    
    content = "🚀 **最新のIT記事（過去6時間）**\n\n"
    for article in articles:
        content += f"- [{article['title']}]({article['url']})\n"

    payload = {"content": content}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    main()
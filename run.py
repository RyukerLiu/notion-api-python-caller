from dotenv import load_dotenv
import requests
import json
import os

# 讀取 .env 文件
load_dotenv()

# 從環境變數中獲取值
notion_key = os.getenv("NOTION_KEY")
notion_database_id = os.getenv("NOTION_DATABASE_ID")

# Notion API
url = "https://api.notion.com/v1/pages/"

payload = json.dumps(
    {
        "parent": {"database_id": notion_database_id},
        "properties": {
            "title": {"title": [{"text": {"content": "Created by Python Caller"}}]}
        },
    }
)
headers = {
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22",
    "Authorization": "Bearer " + notion_key,
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

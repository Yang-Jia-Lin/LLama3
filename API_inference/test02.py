import requests


import os
from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    raise ValueError("API Key not found!")


API_URL = "https://router.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct"

headers = {"Authorization": f"Bearer {API_TOKEN}"}
payload = {
    "inputs": "你好，请介绍一下你自己。",
    "parameters": {"max_new_tokens": 50}
}
response = requests.post(API_URL, headers=headers, json=payload)

# --- 调试 ---
print(f"状态码: {response.status_code}") # 如果不是 200，说明请求失败
print(f"返回内容: {response.text}")      # 打印服务器到底返回了什么文本
if response.status_code == 200:
    print("解析结果:", response.json())
else:
    print("请求失败，请检查 URL 或 Token。")
import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"

response = requests.post(API_URL, json={"inputs":"hello,"})
print(response.json)
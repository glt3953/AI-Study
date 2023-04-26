import os, requests, json

API_TOKEN = os.environ.get("HUGGINGFACE_API_KEY")

model = "Helsinki-NLP/opus-mt-en-zh"

API_URL = f"https://api-inference.huggingface.co/models/{model}"
headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}

def query(payload, api_url=API_URL, headers=headers):
    data = json.dumps(payload)
    response = requests.request("POST", api_url, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

# 翻译文件
with open('data/wwdc2019-423-demo.txt') as f:
    for line in f:
        content = line
        data = query({"inputs" : content, "wait_for_model" : True})
        print(data)
        with open('data/wwdc2019-423-demo-zh.txt', 'a', encoding='utf-8') as f:
            f.write(''.join(data[0].values()) + '\n') # 将dict的值连接为字符串

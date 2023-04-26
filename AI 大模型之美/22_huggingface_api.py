import os, requests, json

API_TOKEN = os.environ.get("HUGGINGFACE_API_KEY")

#model = "google/flan-t5-xxl"
model = "Helsinki-NLP/opus-mt-en-zh"
#model = "hfl/chinese-pert-base"

API_URL = f"https://api-inference.huggingface.co/models/{model}"
headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}

def query(payload, api_url=API_URL, headers=headers):
    data = json.dumps(payload)
    response = requests.request("POST", api_url, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

#question = "Please answer the following question. What is the capital of France?"
question = "My name is Wolfgang and I live in Berlin"
#question = "今天天气真不错！"
data = query({"inputs" : question, "wait_for_model" : True})

print(data)

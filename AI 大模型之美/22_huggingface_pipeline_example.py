import torch
from transformers import pipeline

torch.cuda.is_available()

classifier = pipeline(task="sentiment-analysis", device=0)
preds = classifier("I am really happy today!")
print(preds)

classifier = pipeline(task="sentiment-analysis", model="uer/roberta-base-finetuned-jd-binary-chinese", device=0)
preds = classifier("这个餐馆太难吃了。")
print(preds)

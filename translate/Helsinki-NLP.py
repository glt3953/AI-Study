import torch
torch.cuda.is_available()

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh")

text = "I like to learn data science and AI."
# text = "我喜欢学习数据科学和人工智能。"

# 翻译文件
# with open('drive/MyDrive/colab_data/article/wwdc2019-423.txt') as f:
#     for line in f:
#         content = line
#         translated_text = translation(content)
#         print(translated_text)
#         with open('drive/MyDrive/colab_data/article/wwdc2019-423-zh.txt', 'a', encoding='utf-8') as f:
#           f.write(''.join(translated_text[0].values()) + '\n') # 将dict的值连接为字符串

translated_text = model.translate(text)

print(translated_text)

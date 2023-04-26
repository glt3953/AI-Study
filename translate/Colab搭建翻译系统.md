# Colab搭建翻译系统
1. 使用免费的 Colab Notebook 环境
https://colab.research.google.com
2. 安装 transformers 的相关的依赖包
```
%pip install transformers
%pip install sentencepiece
%pip install sacremoses
```
3. 挂载Google Drive
```
from google.colab import drive

drive.mount('/content/drive')
```
4. 开始翻译
```
from transformers import pipeline

translation = pipeline(task="translation_en_to_zh", model="Helsinki-NLP/opus-mt-en-zh", device=0)
# translation = pipeline(task="translation_zh_to_en", model="Helsinki-NLP/opus-mt-zh-en", device=0)
# translation = pipeline(task="translation_zh_to_en", model="facebook/nllb-200-distilled-600M", device=0)

# text = "I like to learn data science and AI."
# text = "我喜欢学习数据科学和人工智能。"
# 翻译文件
with open('drive/MyDrive/colab_data/article/wwdc2019-423.txt') as f:
  # content = f.read() #读取所有内容
    # inputs = f.readlines() #读取所有行
    for line in f:
        content = line
        translated_text = translation(content)
        print(translated_text)
        with open('drive/MyDrive/colab_data/article/wwdc2019-423-zh.txt', 'a', encoding='utf-8') as f:
          f.write(''.join(translated_text[0].values()) + '\n') # 将dict的值连接为字符串

# translated_text = translation(content)

# with open('drive/MyDrive/colab_data/article/wwdc2019-423-1-zh.txt', 'w', encoding='utf-8') as f:
#     f.write(''.join(translated_text[0].values())) # 将dict的值连接为字符串

# translated_text = translation(text)
# print(translated_text)
```
5. Helsinki-NLP模型

https://huggingface.co/Helsinki-NLP
英语-中文：
https://huggingface.co/Helsinki-NLP/opus-mt-en-zh?text=My+name+is+Wolfgang+and+I+live+in+Berlin
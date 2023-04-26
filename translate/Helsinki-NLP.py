from transformers import pipeline

translation = pipeline(task="translation_en_to_zh", model="Helsinki-NLP/opus-mt-en-zh", device=0)
#translation = pipeline(task="translation_zh_to_en", model="Helsinki-NLP/opus-mt-zh-en", device=0)

text = "I like to learn data science and AI."
#text = "我喜欢学习数据科学和人工智能。"
translated_text = translation(text)
print(translated_text)

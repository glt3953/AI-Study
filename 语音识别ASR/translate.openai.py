import tiktoken
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")
encoding = tiktoken.get_encoding("cl100k_base")

def text_translate(text: str) -> str:
  if len(text) == 0:
    print("待翻译文本为空")
  
  prompt = '将以下内容翻译为英文：' + text
  print('prompt：' + prompt)
  
  if len(encoding.encode(prompt)) > 512:
    return "您的提示语过长，请精简后再试"

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", #gpt-4, gpt-3.5-turbo, text-embedding-ada-002
    messages=[{"role": "user", "content": prompt}],
    temperature=0.5,
    max_tokens=3580,
    top_p=1)
    
  result = '按照您的提示语：' + prompt + '，翻译的文案如下：\n\n' + response["choices"][0]["message"]["content"]
    
  print(result)

  return result

text_translate("")

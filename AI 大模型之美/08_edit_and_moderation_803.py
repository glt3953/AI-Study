import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def moderation(text):
    response = openai.Moderation.create(
        input=text
    )
    output = response["results"][0]
    return output
    
def chatgpt(text):
    messages = []
    messages.append( {"role": "system", "content": "You are a useful AI assistant"})
    messages.append( {"role": "user", "content": text})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
    )
    message = response["choices"][0]["message"]["content"]
    return message

threaten = "你不听我的我就拿刀砍死你"
#print(chatgpt(threaten))
print(moderation(threaten))

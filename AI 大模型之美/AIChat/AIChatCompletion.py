#依赖tiktoken：pip install tiktoken，使用不同的 GPT 模型，对应着不同的 Tiktoken 的编码器模型：https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb。
import tiktoken
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")
encoding = tiktoken.get_encoding("cl100k_base")

class Conversation:
    def __init__(self, prompt, num_of_round):
        self.prompt = prompt
        self.num_of_round = num_of_round
        self.messages = []
        self.messages.append({"role": "system", "content": self.prompt})

    def ask(self, question):
        try:
            if len(encoding.encode(question)) > 512:
                return "输入的文字过长，请精简后再提问"
        
            self.messages.append({"role": "user", "content": question})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", #gpt-4, gpt-3.5-turbo, text-embedding-ada-002
                messages=self.messages,
                temperature=0.5,
                max_tokens=3580,
                top_p=1,
            )
        except Exception as e:
            print(e)
            return e

        message = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": message})

        if len(self.messages) > self.num_of_round*2 + 1:
            del self.messages[1:3] #Remove the first round conversation left.
            
        return message
        
print("你好，我是一个聊天机器人，请你提出你的问题吧")

prompt = """你好，我是一个聊天机器人，请你提出你的问题吧"""
conv = Conversation(prompt, 10)

while True:
    user_input = input("> ")
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Goodbye!")
        break
    
    answer = conv.ask(user_input)
    print(answer)

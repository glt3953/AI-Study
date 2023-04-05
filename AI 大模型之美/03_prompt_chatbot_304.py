#依赖tiktoken：pip install tiktoken，使用不同的 GPT 模型，对应着不同的 Tiktoken 的编码器模型：https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb。
import tiktoken
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]
encoding = tiktoken.get_encoding("p50k_base")

def ask_gpt3(prompt):
    if len(encoding.encode(prompt)) > 512:
        return "输入的文字过长，请精简后再提问"
            
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3580,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

print("你好，我是一个聊天机器人，请你提出你的问题吧?")

questions = []
answers = []

def generate_prompt(prompt, questions, answers):
    num = len(answers)
    for i in range(num):
        prompt += "\n Q : " + questions[i]
        prompt += "\n A : " + answers[i]
    prompt += "\n Q : " + questions[num] + "\n A : "        
    return prompt

while True:
    user_input = input("> ")
    questions.append(user_input)
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Goodbye!")
        break
    
    prompt = generate_prompt("", questions, answers)

    answer = ask_gpt3(prompt)
    print(answer)
    answers.append(answer)

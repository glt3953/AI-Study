from transformers import T5ForConditionalGeneration, T5Tokenizer

import torch

# load the T5 tokenizer and model
tokenizer = T5Tokenizer.from_pretrained('t5-base')
model = T5ForConditionalGeneration.from_pretrained('t5-base')

def generate_answer(question):
    input_text = 'answer: ' + question + ' </s>'
    features = tokenizer([input_text], return_tensors='pt')
    output = model.generate(input_ids=features['input_ids'], 
                            attention_mask=features['attention_mask'])
    return tokenizer.decode(output[0], skip_special_tokens=True)

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

    answer = generate_answer(prompt)
    print(answer)
    answers.append(answer)
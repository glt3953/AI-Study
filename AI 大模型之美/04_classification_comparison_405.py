from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained('t5-large')
tokenizer = T5Tokenizer.from_pretrained('t5-large', model_max_length=512)

def generate_answer(question):
    # input_text = 'answer: ' + question + ' </s>'
    input_text = 'answer: ' + question
    features = tokenizer([input_text], return_tensors='pt')
    output = model.generate(input_ids=features['input_ids'], 
                            attention_mask=features['attention_mask'], max_new_tokens=512)
    return tokenizer.decode(output[0], skip_special_tokens=True)

while True:
    # 接受用户输入
    input_text = input("用户: ")
    
    # 如果用户要求退出，程序将停止
    if input_text.strip().lower() == '退出':
        break
    
    # 生成回答
    answer = generate_answer(input_text)
    
    # 输出回答
    print("AI助手: " + answer)
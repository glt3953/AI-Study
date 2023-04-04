from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained('t5-large')
tokenizer = T5Tokenizer.from_pretrained('t5-large', model_max_length=512)

def translate_answer(question):
    input_ids = tokenizer.encode(question, return_tensors='pt')
    outputs = model.generate(input_ids, max_new_tokens=512)
    output_str = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output_str

print("你好，我是一个翻译机器人，请你说出需要翻译的内容吧？")

while True:
    # 接受用户输入，示例：translate English to French: Hello, how are you?
    input_text = input("用户: ")
    
    # 如果用户要求退出，程序将停止
    if input_text.strip().lower() == '退出':
        break
    
    # 生成回答
    answer = translate_answer(input_text)
    
    # 输出回答
    print("AI助手: " + answer)
# Output: Bonjour, comment vas-tu?
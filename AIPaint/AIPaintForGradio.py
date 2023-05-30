#安装一下 Python 的 Gradio 的包：conda install -c conda-forge gradio
import gradio as gr
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
      
def paint(prompt):
    try:
        #惊蛰万物苏醒，清明踏青，秋分桂花飘香，大寒赏雪。
        #晴方好，雨亦奇，来几日，见彩霏。花遮著，人掩扉，但自知，春色在。
        #三月春归，草长莺飞。伴着疫情的寒冬远去，一个崭新的春天正在走近。和春天一起回归的，还有林野间的绚烂山桃花海。
        #落花人独立，微雨燕双飞。
        response = openai.Image.create(
          prompt=prompt,
          n=2,
          size="1024x1024"
        )
    except Exception as e:
        print(e)
        return e

    return response

print("你是一位画家，需要根据用户的描述画出两幅作品，提供相应的url地址")

with gr.Blocks(css="#chatbot{height:300px} .overflow-y-auto{height:500px}") as demo:
    chatbot = gr.Chatbot(elem_id="chatbot")
    state = gr.State([])

    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)

    txt.submit(answer, [txt, state], [chatbot, state])

demo.launch()

while True:
    user_input = input("> ")
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Goodbye!")
        break
    
    response = paint(user_input)
    
    print("生成的图片地址如下: \n%s\n%s" % (response["data"][0]["url"], response["data"][1]["url"]))

import os, time, requests
import gradio as gr
from gradio import HTML

avatar_url = "https://cdn.discordapp.com/attachments/1065596492796153856/1095617463112187984/John_Carmack_Potrait_668a7a8d-1bb0-427d-8655-d32517f6583d.png"

def generate_talk(input, avatar_url,
                  voice_type = "microsoft",
                  voice_id = "zh-CN-YunyeNeural",
                  api_key = os.environ.get('DID_API_KEY')):
    url = "https://api.d-id.com/talks"
    payload = {
        "script": {
            "type": "text",
            "provider": {
                "type": voice_type,
                "voice_id": voice_id
            },
            "ssml": "false",
            "input": input
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0"
        },
        "source_url": avatar_url
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic " + api_key
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def get_a_talk(id, api_key = os.environ.get('DID_API_KEY')):
    url = "https://api.d-id.com/talks/" + id
    headers = {
        "accept": "application/json",
        "authorization": "Basic "+api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

#result_url 字段会在服务器端把整个视频生成完成之后才出现，所以我们需要循环等待。
def get_mp4_video(input, avatar_url=avatar_url):
    response = generate_talk(input=input, avatar_url=avatar_url)
    talk = get_a_talk(response['id'])
    video_url = ""
    index = 0
    while index < 300:
        index += 1
        if 'result_url' in talk:
            video_url = talk['result_url']
            print(talk)
            return video_url
        else:
            time.sleep(1)
            talk = get_a_talk(response['id'])
            print(talk)
    return video_url

def predict(input, history=[]):
    if input is not None:
        history.append(input)
        response = '我是您的工作助手'
        video_url = get_mp4_video(input=response, avatar_url=avatar_url)
        video_html = f"""<video width="320" height="240" controls autoplay><source src="{video_url}" type="video/mp4"></video>"""
        history.append(response)
        responses = [(u,b) for u,b in zip(history[::2], history[1::2])]
        return responses, video_html, history
    else:
        video_html = f'<img src="{avatar_url}" width="320" height="240" alt="John Carmack">'
        responses = [(u,b) for u,b in zip(history[::2], history[1::2])]
        return responses, video_html, history

with gr.Blocks(css="#chatbot{height:500px} .overflow-y-auto{height:500px}") as demo:
    chatbot = gr.Chatbot(elem_id="chatbot")
    state = gr.State([])

    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)

    with gr.Row():
        video = gr.HTML(f'<img src="{avatar_url}" width="320" height="240" alt="John Carmack">', live=False)

    txt.submit(predict, [txt, state], [chatbot, video, state])
    
demo.launch()

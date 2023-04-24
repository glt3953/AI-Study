import openai, os
import gradio as gr
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from paddlespeech.cli.tts.infer import TTSExecutor
import pygame #pygame - 跨平台,支持更多格式的音频文件,如.wav,.mp3,.ogg等。

openai.api_key = os.environ["OPENAI_API_KEY"]

memory = ConversationSummaryBufferMemory(llm=ChatOpenAI(), max_token_limit=2048)
conversation = ConversationChain(
    llm=OpenAI(max_tokens=2048, temperature=0.5),
    memory=memory,
)

tts_executor = TTSExecutor()
pygame.mixer.init()
def play_voice(text):
    output_file = "./data/text.wav"
    tts_executor(text=text, output=output_file)
    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()

def predict(input, history=[]):
    history.append(input)
    response = conversation.predict(input=input)
    history.append(response)
    play_voice(response)
    responses = [(u,b) for u,b in zip(history[::2], history[1::2])]
    return responses, history
    
def transcribe(audio):
    os.rename(audio, audio + '.wav')
    audio_file = open(audio + '.wav', "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']
    
def process_audio(audio, history=[]):
    text = transcribe(audio)
    return predict(text, history)

with gr.Blocks(css="#chatbot{height:800px} .overflow-y-auto{height:800px}") as demo:
    chatbot = gr.Chatbot(elem_id="chatbot")
    state = gr.State([])

    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)
        
    with gr.Row():
        audio = gr.Audio(source="microphone", type="filepath")
        
    txt.submit(predict, [txt, state], [chatbot, state])
    audio.change(process_audio, [audio, state], [chatbot, state])

demo.launch()

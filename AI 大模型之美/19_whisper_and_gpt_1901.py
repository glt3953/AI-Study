import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file= open("./data/podcast_clip.mp3", "rb")
#transcript = openai.Audio.transcribe("whisper-1", audio_file)
#transcript = openai.Audio.transcribe("whisper-1", audio_file, prompt="这是一段中文播客内容。")
#transcript = openai.Audio.transcribe("whisper-1", audio_file, prompt="这是一段Onboard播客的内容。")
transcript = openai.Audio.transcribe("whisper-1", audio_file, prompt="这是一段Onboard播客，里面会聊到ChatGPT以及PALM这个大语言模型。这个模型也叫做Pathways Language Model。")
print(transcript['text'])
    
# write to file
with open(f"./data/podcast_clip_openai.txt", "w") as f:
    f.write(transcript['text'])
#transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format="srt", prompt="这是一段Onboard播客，里面会聊到PALM这个大语言模型。这个模型也叫做Pathways Language Model。") #可选参数：language（音频的语言）
#print(transcript)

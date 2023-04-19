import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

index = 11 # number of fi
prompt = "这是一段Onboard播客，里面会聊到ChatGPT以及PALM这个大语言模型。这个模型也叫做Pathways Language Model。"
for i in range(index):
    clip = f"./data/podcast_clip_{i}.mp3"
    audio_file= open(clip, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file,
                                     prompt=prompt)
    # mkdir ./data/transcripts if not exists
    if not os.path.exists("./data/transcripts"):
        os.makedirs("./data/transcripts")
    # write to file
    with open(f"./data/transcripts/podcast_clip_{i}.txt", "w") as f:
        f.write(transcript['text'])
    # get last sentence of the transcript
    sentences = transcript['text'].split("。")
    prompt = sentences[-1]

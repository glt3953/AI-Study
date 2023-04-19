import whisper

model = whisper.load_model("medium") #tiny、base、small、medium（可用）、large
index = 1 # number of fi
  
def transcript(clip, prompt, output):
    result = model.transcribe(clip, initial_prompt=prompt)
    with open(output, "w") as f:
        f.write(result['text'])
    print("Transcripted: ", clip)

original_prompt = "这是一段Onboard播客，里面会聊到ChatGPT以及PALM这个大语言模型。这个模型也叫做Pathways Language Model。\n\n"
prompt = original_prompt
for i in range(index):
    clip = f"./data/podcast_clip.mp3"
    output = f"./data/podcast_clip_medium.txt"
    transcript(clip, prompt, output)
    # get last sentence of the transcript
    with open(output, "r") as f:
        transcript = f.read()
    sentences = transcript.split("。")
    prompt = original_prompt + sentences[-1]

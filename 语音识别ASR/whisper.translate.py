import whisper

model = whisper.load_model("medium") #tiny、base、small、medium（可用）、large

#audio_file= f"./data/podcast_clip.mp3"
audio_file= f"./data/paddlespeech.asr-zh.wav"
#audio_file= f"./data/paddlespeech.asr-en.wav"
translated_prompt="""This is a podcast discussing ChatGPT and PaLM model.
The full name of PaLM is Pathways Language Model."""
result = model.transcribe(audio_file, initial_prompt=translated_prompt)

#output = f"./data/podcast_clip_medium_en.txt"
output = f"./data/paddlespeech.asr-zh_en.txt"
#output = f"./data/paddlespeech.asr-en_en.txt"
with open(output, "w") as f:
    f.write(result['text'])
    
print(result['text'])


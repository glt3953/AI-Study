import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

clip = f"2023-10-24_16-29-39.amr"
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

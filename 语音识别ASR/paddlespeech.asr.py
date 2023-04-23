from paddlespeech.cli.asr.infer import ASRExecutor

asr = ASRExecutor()

#result = asr(audio_file="./data/paddlespeech.asr-zh.wav")
result = asr(audio_file="./data/podcast_clip.mp3")
#result = asr(audio_file="./data/paddlespeech.asr-en.wav")

with open('./data/podcast_clip_paddlespeech.txt', 'w') as f:
#with open('./data/paddlespeech.asr-zh.txt', 'w') as f:
#with open('./data/paddlespeech.asr-en.txt', 'w') as f:
    f.write(result)
print(result)
# 我认为跑步最重要的就是给我带来了身体健康

# TTS与语音合成
## Azure 云
https://azure.microsoft.com/zh-cn/
## 科大讯飞
https://www.xfyun.cn/services/online_tts
## 阿里云
https://ai.aliyun.com/nls/tts
## 百度
https://ai.baidu.com/tech/speech/tts
### 开源的 PaddleSpeech 的语音合成
1. 安装 PaddleSpeech 相关的 Python 包
```
pip install paddlepaddle
pip install paddlespeech
```
2. 通过 PaddleSpeech 自带的 TTSExecutor，可以将对应的文本内容转换成 WAV 文件
```
from paddlespeech.cli.tts.infer import TTSExecutor

tts_executor = TTSExecutor()

text = "今天天气十分不错，百度也能做语音合成。"
output_file = "./data/paddlespeech.wav"
tts_executor(text=text, output=output_file)
```
<!--
3. 要在 Python 里面播放对应的声音，我们还要借助于 PyAudio 这个包。对应的，我们要先安装 PyAudio 依赖的 portaudio 库，然后再安装 PyAudio 包
```
brew install portaudio
pip install pyaudio
```
-->
3. 要在 Python 里面播放对应的声音，我们还要借助于 pygame - 跨平台,支持更多格式的音频文件,如.wav,.mp3,.ogg等。
```
pip install pygame
```
使用示例：
```
import pygame

pygame.mixer.init()
pygame.mixer.music.load(output_file)
pygame.mixer.music.play()
```
## AWS Polly
https://aws.amazon.com/cn/polly/
## Google Cloud
https://cloud.google.com/text-to-speech
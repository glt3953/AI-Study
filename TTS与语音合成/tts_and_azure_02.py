import os
import azure.cognitiveservices.speech as speechsdk

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AZURE_SPEECH_KEY'), region=os.environ.get('AZURE_SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# The language of the voice that speaks.
# SSML 格式的 XML 文件，这个 SSML 是 Speech Synthesis Markup Language 的首字母缩写，翻译过来就是语音合成标记语言。
ssml = """<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="zh-CN">
    <voice name="zh-CN-YunyeNeural">
        儿子看见母亲走了过来，说到：
        <mstts:express-as role="Boy" style="cheerful">
            “妈妈，我想要买个新玩具”
        </mstts:express-as>
    </voice>
    <voice name="zh-CN-XiaomoNeural">
        母亲放下包，说：
        <mstts:express-as role="SeniorFemale" style="angry">
            “我看你长得像个玩具。”
        </mstts:express-as>
    </voice>
</speak>"""

speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml).get()

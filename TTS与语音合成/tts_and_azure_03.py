import os
import azure.cognitiveservices.speech as speechsdk

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AZURE_SPEECH_KEY'), region=os.environ.get('AZURE_SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(filename="./data/tts.wav")

# The language of the voice that speaks.
speech_config.speech_synthesis_language='zh-CN'
speech_config.speech_synthesis_voice_name='zh-CN-XiaohanNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

text = "今天天气真不错，ChatGPT真好用"
speech_synthesizer.speak_text_async(text)

#speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio48Khz192KBitRateMonoMp3)
#
#speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
#result = speech_synthesizer.speak_text_async(text).get()
#stream = speechsdk.AudioDataStream(result)
#
#stream.save_to_wav_file("./data/tts.mp3")

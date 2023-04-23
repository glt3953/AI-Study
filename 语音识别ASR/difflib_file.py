import difflib

audio_file= open("./data/paddlespeech.asr-zh.wav", "rb")
text1 = """Hello
This is a text
With several lines
"""

text2 = """Hello
This is a text
With different lines
"""

diff = difflib.ndiff(text1.splitlines(keepends=True), text2.splitlines(keepends=True))
#diff = difflib.context_diff(text1.splitlines(keepends=True), text2.splitlines(keepends=True))
print(''.join(diff), end='')

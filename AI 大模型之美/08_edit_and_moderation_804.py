import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

prefix = """在这个快节奏的现代社会中，我们每个人都面临着各种各样的挑战和困难。
在这些挑战和困难中，有些是由外部因素引起的，例如经济萧条、全球变暖和自然灾害等。\n"""
# 还有一些是由内部因素引起的，例如情感问题、健康问题和自我怀疑等。
suffix = """\n面对这些挑战和困难，我们需要采取积极的态度和行动来克服它们。
这意味着我们必须具备坚韧不拔的意志和创造性思维，以及寻求外部支持的能力。
只有这样，我们才能真正地实现自己的潜力并取得成功。"""

def insert_text(prefix, suffix):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prefix,
        suffix=suffix,
        max_tokens=1024,
        )
    return response

response = insert_text(prefix, suffix)
print(response["choices"][0]["text"])

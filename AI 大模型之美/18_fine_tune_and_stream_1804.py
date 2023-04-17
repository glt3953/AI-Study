import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def write_a_story(prompt):
    response = openai.Completion.create(
        model="curie:ft-bothub-ai:ultraman-2023-04-04-03-03-26",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        stop=["."])
    return response["choices"][0]["text"]

story = write_a_story("宋,发射激光,艰难 ->\n")
print(story)

story = write_a_story("秦,龙卷风,辛苦 ->\n")
print(story)

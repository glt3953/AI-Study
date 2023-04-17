import os,openai,backoff
import pandas as pdopenai.api_key = os.environ.get("OPENAI_API_KEY")

#openai.api_key = os.getenv("OPENAI_API_KEY")

dynasties= ['唐', '宋', '元', '明', '清', '汉', '魏', '晋', '南北朝']
super_powers = ['隐形', '飞行', '读心术', '瞬间移动', '不死之身', '喷火']
story_types = ['轻松', '努力', '艰难']

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def gpt35(prompt, max_tokens=2048, temperature=0.5, top_p=1, frequency_penalty=0, presence_penalty=0):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty)
    return response["choices"][0]["text"]

def prepare_stories(dynasties, super_powers, story_types, output_file="data/ultraman_stories.csv"):
    df = pd.DataFrame()
    repeat = 3
    for dynasty in dynasties:
        for super_power in super_powers:
            for story_type in story_types:
                   for i in range(repeat):
                        prompt = f"""请你用中文写一段300字的故事，情节跌宕起伏，讲述一位{dynasty}朝时期的英雄人物，穿越到现代，拥有了{super_power}这样的超能力，通过{story_type}的战斗，帮助奥特曼一起打败了怪兽的故事。"""
                        story = gpt35(prompt)
                        row = {"dynasty": dynasty, "super_power": super_power, "story_type": story_type, "story": story}
                        row = pd.DataFrame([row])
                        df = pd.concat([df, row], axis=0, ignore_index=True)

    df.to_csv("data/ultraman_stories.csv")

prepare_stories(dynasties, super_powers, story_types)

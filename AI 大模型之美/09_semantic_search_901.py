import openai, os
import pandas as pd
from IPython.display import display

openai.api_key = os.environ.get("OPENAI_API_KEY")
COMPLETION_MODEL = "text-davinci-003"

def generate_data_by_prompt(prompt):
    response = openai.Completion.create(
        engine=COMPLETION_MODEL,
        prompt=prompt,
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
    )
    return response.choices[0].text

prompt = """请你生成50条淘宝网里的商品的标题，每条在30个字左右，品类是3C数码产品，标题里往往也会有一些促销类的信息，每行一条。"""
#prompt = """请你生成50条京东商城里最受欢迎的小家电信息，包含购物链接，每条在30个字左右，每行一条。"""
data = generate_data_by_prompt(prompt)
product_names = data.strip().split('\n')
df = pd.DataFrame({'product_name': product_names})
df.product_name = df.product_name.apply(lambda x: x.split('.')[1].strip())
df.head()

#clothes_prompt = """请你生成50条淘宝网里的商品的标题，每条在30个字左右，品类是女性的服饰箱包等等，标题里往往也会有一些促销类的信息，每行一条。"""
#clothes_data = generate_data_by_prompt(clothes_prompt)
#clothes_product_names = clothes_data.strip().split('\n')
#clothes_df = pd.DataFrame({'product_name': clothes_product_names})
#clothes_df.product_name = clothes_df.product_name.apply(lambda x: x.split('.')[1].strip())
#clothes_df.head()
#
#df = pd.concat([df, clothes_df], axis=0)
df = df.reset_index(drop=True)
display(df)
#df.to_parquet("data/taobao_product_info.parquet", index=False)
df.to_csv('data/100_productsinfo.csv', index=False)
#out = pd.merge(df, targets, left_on='target', right_index=True)
#out.to_csv('100_productsinfo.csv', index=False)

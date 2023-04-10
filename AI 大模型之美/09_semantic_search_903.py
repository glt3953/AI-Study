from openai.embeddings_utils import get_embedding, cosine_similarity
import openai, os, backoff
from IPython.display import display
import pandas as pd

openai.api_key = os.environ.get("OPENAI_API_KEY")
COMPLETION_MODEL = "text-davinci-003"
embedding_model = "text-embedding-ada-002"

def generate_data_by_prompt(prompt):
    response = openai.Completion.create(
        engine=COMPLETION_MODEL,
        prompt=prompt,
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
    )
    return response.choices[0].text

prompt = """请你生成100条淘宝网里的商品的标题，每条在30个字左右，品类是3C数码产品，标题里往往也会有一些促销类的信息，每行一条。"""
data = generate_data_by_prompt(prompt)
product_names = data.strip().split('\n')
df = pd.DataFrame({'product_name': product_names})
df.product_name = df.product_name.apply(lambda x: x.split('.')[0].strip())
df.head()

batch_size = 100

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def get_embeddings_with_backoff(prompts, engine):
    embeddings = []
    for i in range(0, len(prompts), batch_size):
        batch = prompts[i:i+batch_size]
        embeddings += get_embeddings(prompts=batch, engine=engine)
    return embeddings

prompts = df.product_name.tolist()
prompt_batches = [prompts[i:i+batch_size] for i in range(0, len(prompts), batch_size)]

embeddings = []
for batch in prompt_batches:
    batch_embeddings = get_embeddings_with_backoff(prompts=batch, engine=embedding_model)
    embeddings += batch_embeddings

df["embedding"] = embeddings
df.to_parquet("data/taobao_3C_product_title.parquet", index=False)

def recommend_product(df, product_name, n=3, pprint=True):
    product_embedding = df[df['product_name'] == product_name].iloc[0].embedding
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, product_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
        .product_name
    )
    if pprint:
        for r in results:
            print(r)
    return results

results = recommend_product(df, "【限量】OnePlus 7T Pro 8GB+256GB 全网通", n=3)
display(results)

import openai, os
from langchain.llms import OpenAI
from langchain.chains import LLMRequestsChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import TransformChain, SequentialChain
import pandas as pd
from IPython.display import display

openai.api_key = os.environ.get("OPENAI_API_KEY")

template = """在 >>> 和 <<< 直接是来自Google的原始搜索结果.
请把对于问题 '{query}' 的答案从里面提取出来，如果里面没有相关信息的话就说 "找不到"
请使用如下格式：
Extracted:<answer or "找不到">
>>> {requests_result} <<<
Extracted:"""

PROMPT = PromptTemplate(
    input_variables=["query", "requests_result"],
    template=template,
)
requests_chain = LLMRequestsChain(llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=PROMPT))
#question = "近一个月最受欢迎的50个小家电（价格在50-300元）及其购买链接"
question = "中国北京去往银川的直达以及中转火车车次信息？"
inputs = {
    "query": question,
    "url": "https://www.google.com/search?q=" + question.replace(" ", "+")
}

result=requests_chain(inputs)
#product_names = result.strip().split('\n')
#df = pd.DataFrame({'product_name': product_names})
#df = pd.DataFrame({'product_name': result})
#df.product_name = df.product_name.apply(lambda x: x.split('.')[1].strip())
#df.head()
#df = df.reset_index(drop=True)
#df.to_csv('data/taobao_small_productsinfo.csv', index=False)

print(result['output'])

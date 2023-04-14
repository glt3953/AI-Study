import openai, os
from langchain import OpenAI
from langchain.agents import initialize_agent, tool, Tool

openai.api_key = os.environ.get("OPENAI_API_KEY")

llm = OpenAI(temperature=0)

import json

ORDER_1 = "20230101ABC"
ORDER_2 = "20230101EFG"

ORDER_1_DETAIL = {
    "order_number": ORDER_1,
    "status": "已发货",
    "shipping_date" : "2023-01-03",
    "estimated_delivered_date": "2023-01-05",
}

ORDER_2_DETAIL = {
    "order_number": ORDER_2,
    "status": "未发货",
    "shipping_date" : None,
    "estimated_delivered_date": None,
}

import re

@tool("Search Order")
def search_order(input:str)->str:
    """一个帮助用户查询最新订单状态的工具，并且能处理以下情况：
    1. 在用户没有输入订单号的时候，会询问用户订单号
    2. 在用户输入的订单号查询不到的时候，会让用户二次确认订单号是否正确"""
    pattern = r"\d+[A-Z]+"
    match = re.search(pattern, input)

    order_number = input
    if match:
        order_number = match.group(0)
    else:
        return "请问您的订单号是多少？"
    if order_number == ORDER_1:
        return json.dumps(ORDER_1_DETAIL)
    elif order_number == ORDER_2:
        return json.dumps(ORDER_2_DETAIL)
    else:
        return f"对不起，根据{input}没有找到您的订单"
    
@tool("FAQ")
def faq(intput: str) -> str:
    """"useful for when you need to answer questions about shopping policies, like return policy, shipping policy, etc."""
    return faq_chain.run(intput)

@tool("Recommend Product")
def recommend_product(input: str) -> str:
    """"useful for when you need to search and recommend products and recommend it to the user"""
    return product_chain.run(input)

#tools = [
#    Tool(
#        name = "Search Order",func=search_order,
#        description="useful for when you need to answer questions about customers orders"
#    ),
#    recommend_product, faq]
#
#agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

tools = [search_order,recommend_product, faq]
agent = initialize_agent(tools, llm=OpenAI(temperature=0), agent="zero-shot-react-description", verbose=True)

question = "我有一张订单，订单号是 2022ABCDE，一直没有收到，能麻烦帮我查一下吗？"
answer = agent.run(question)
print(answer)

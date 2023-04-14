import openai, os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain import OpenAI, VectorDBQA
from langchain.agents import initialize_agent, tool, Tool
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import CSVLoader

openai.api_key = os.environ.get("OPENAI_API_KEY")

llm = OpenAI(temperature=0)

product_loader = CSVLoader('./data/ecommerce_products.csv')
product_documents = product_loader.load()
product_text_splitter = CharacterTextSplitter(chunk_size=1024, separator="\n")
product_texts = product_text_splitter.split_documents(product_documents)
product_search = FAISS.from_documents(product_texts, OpenAIEmbeddings())
product_chain = VectorDBQA.from_chain_type(llm=llm, vectorstore=product_search, verbose=True)

def search_order(input: str) -> str:
    return "订单状态：已发货；发货日期：2023-01-01；预计送达时间：2023-01-10"
    
@tool("FAQ")
def faq(intput: str) -> str:
    """"useful for when you need to answer questions about shopping policies, like return policy, shipping policy, etc."""
    return faq_chain.run(intput)

@tool("Recommend Product")
def recommend_product(input: str) -> str:
    """"useful for when you need to search and recommend products and recommend it to the user"""
    return product_chain.run(input)

tools = [
    Tool(
        name = "Search Order",func=search_order,
        description="useful for when you need to answer questions about customers orders"
    ),
    recommend_product, faq]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

question = "我想买一件衣服，想要在春天去公园穿，但是不知道哪个款式好看，你能帮我推荐一下吗？"
answer = agent.run(question)
print(answer)

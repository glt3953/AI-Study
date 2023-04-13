import openai, os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory

openai.api_key = os.environ.get("OPENAI_API_KEY")

template = """你是一个中国厨师，用中文回答做菜的问题。你的回答需要满足以下要求:
1. 你的回答必须是中文
2. 回答限制在100个字以内

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template
)
memory = ConversationBufferWindowMemory(memory_key="chat_history", k=3)
llm_chain = LLMChain(
    llm=OpenAI(),
    prompt=prompt,
    memory=memory,
    verbose=True
)
llm_chain.predict(human_input="你是谁？")
llm_chain.predict(human_input="鱼香肉丝怎么做？")
llm_chain.predict(human_input="那宫保鸡丁呢？")
llm_chain.predict(human_input="我问你的第一句话是什么？")
answer = llm_chain.predict(human_input="我问你的第一句话是什么？")
print(answer)

memory.load_memory_variables({})

import openai, os
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

openai.api_key = os.environ.get("OPENAI_API_KEY")

llm = OpenAI(temperature=0)
entityMemory = ConversationEntityMemory(llm=llm)
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=entityMemory
)

answer=conversation.predict(input="我叫张老三，在你们这里下了一张订单，订单号是 2023ABCD，我的邮箱地址是 customer@abc.com，但是这个订单十几天了还没有收到货")
print(answer)

#print(conversation.memory.entity_store.store)
print(conversation.memory.store)

answer=conversation.predict(input="我刚才的订单号是多少？")
print(answer)

answer=conversation.predict(input="订单2023ABCD是谁的订单？")
print(answer)

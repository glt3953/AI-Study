import openai, os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

openai.api_key = os.environ.get("OPENAI_API_KEY")

documents = SimpleDirectoryReader('./data/mr_fujino').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

index.save_to_disk('index_mr_fujino.json')

index = GPTSimpleVectorIndex.load_from_disk('index_mr_fujino.json')
response = index.query("鲁迅先生在日本学习医学的老师是谁？")
print(response)

response = index.query("鲁迅先生去哪里学的医学？")
print(response)

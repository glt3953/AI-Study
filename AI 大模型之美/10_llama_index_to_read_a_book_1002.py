#import openai, os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from llama_index import QuestionAnswerPrompt

#openai.api_key = os.environ.get("OPENAI_API_KEY")

documents = SimpleDirectoryReader('./data/mr_fujino').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)
index.save_to_disk('index_mr_fujino.json')
index = GPTSimpleVectorIndex.load_from_disk('index_mr_fujino.json')

query_str = "鲁迅先生在日本学习医学的老师是谁？"
#query_str = "鲁迅先生去哪里学的医学？"
DEFAULT_TEXT_QA_PROMPT_TMPL = (
    "Context information is below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the question: {query_str}\n"
)
QA_PROMPT = QuestionAnswerPrompt(DEFAULT_TEXT_QA_PROMPT_TMPL)

response = index.query(query_str, text_qa_template=QA_PROMPT)
print(response)

response= index.query("请问林黛玉和贾宝玉是什么关系？", text_qa_template=QA_PROMPT)
print(response)

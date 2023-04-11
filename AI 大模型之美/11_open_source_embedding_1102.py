import locale
locale.getpreferredencoding = lambda: "UTF-8"

import openai, os
import faiss
from llama_index import SimpleDirectoryReader, LangchainEmbedding, GPTFaissIndex, ServiceContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from llama_index.node_parser import SimpleNodeParser

from langchain.llms.base import LLM
from llama_index import LLMPredictor
from typing import Optional, List, Mapping, Any

class CustomLLM(LLM):
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response, history = model.chat(tokenizer, prompt, history=[])
        # only return newly generated tokens
        return response

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"name_of_model": "chatglm-6b-int4"}

    @property
    def _llm_type(self) -> str:
        return "custom"
        
from langchain.text_splitter import SpacyTextSplitter

llm_predictor = LLMPredictor(llm=CustomLLM())

text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=100, chunk_overlap=20)
parser = SimpleNodeParser(text_splitter=text_splitter)
documents = SimpleDirectoryReader('./drive/MyDrive/colab_data/faq/').load_data()
nodes = parser.get_nodes_from_documents(documents)

embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
))
service_context = ServiceContext.from_defaults(embed_model=embed_model, llm_predictor=llm_predictor)

dimension = 768
faiss_index = faiss.IndexFlatIP(dimension)
index = GPTFaissIndex(nodes=nodes, faiss_index=faiss_index, service_context=service_context)

from llama_index import QuestionAnswerPrompt
from llama_index import QueryMode

QA_PROMPT_TMPL = (
    "{context_str}"
    "\n\n"
    "根据以上信息，请回答下面的问题：\n"
    "Q: {query_str}\n"
    )
QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)

response = index.query(
    "请问你们海南能发货吗？",
    mode=QueryMode.EMBEDDING,
    text_qa_template=QA_PROMPT,
    verbose=True,
)
print(response)

import openai
import os
from openai.embeddings_utils import cosine_similarity, get_embedding

openai.api_key = os.environ.get("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-ada-002"

positive_review = get_embedding("好评")
negative_review = get_embedding("差评")

good_restraurant = get_embedding("这家餐馆太好吃了，一点都不糟糕")
bad_restraurant = get_embedding("这家餐馆太糟糕了，一点都不好吃")

def get_score(sample_embedding):
  return cosine_similarity(sample_embedding, positive_review) - cosine_similarity(sample_embedding, negative_review)

good_score = get_score(good_restraurant)
bad_score = get_score(bad_restraurant)
print("好评餐馆的评分 : %f" % (good_score))
print("差评餐馆的评分 : %f" % (bad_score))
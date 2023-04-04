
import pandas as pd
import torch

from sklearn.metrics import classification_report
from transformers import T5Tokenizer, T5Model
from openai.embeddings_utils import cosine_similarity

# load the T5 tokenizer and model
tokenizer = T5Tokenizer.from_pretrained('t5-large', model_max_length=512)
model = T5Model.from_pretrained('t5-large')

datafile_path = "data/fine_food_reviews_with_embeddings_1k.csv"

# encode the input sentence
def get_t5_vector(line):
    input_ids = tokenizer.encode(line, return_tensors='pt', max_length=512, truncation=True)
    # generate the vector representation
    with torch.no_grad():
        outputs = model.encoder(input_ids=input_ids)
        vector = outputs.last_hidden_state.mean(dim=1)
    return vector[0]

positive_review_in_t5 = get_t5_vector("An Amazon review with a positive sentiment.")
negative_review_in_t5 = get_t5_vector('An Amazon review with a negative sentiment.')

df = pd.read_csv(datafile_path)

df["t5_embedding"] = df.Text.apply(get_t5_vector)
# convert 5-star rating to binary sentiment
df = df[df.Score != 3]
df["sentiment"] = df.Score.replace({1: "negative", 2: "negative", 4: "positive", 5: "positive"})

from sklearn.metrics import PrecisionRecallDisplay
def evaluate_embeddings_approach():
    def label_score(review_embedding):
        return cosine_similarity(review_embedding, positive_review_in_t5) - cosine_similarity(review_embedding, negative_review_in_t5)

    probas = df["t5_embedding"].apply(lambda x: label_score(x))
    preds = probas.apply(lambda x: 'positive' if x>0 else 'negative')

    report = classification_report(df.sentiment, preds)
    print(report)

    display = PrecisionRecallDisplay.from_predictions(df.sentiment, probas, pos_label='positive')
    _ = display.ax_.set_title("2-class Precision-Recall curve")

evaluate_embeddings_approach()
import torch
from transformers import pipeline

detector = pipeline(model="google/owlvit-base-patch32", task="zero-shot-object-detection")
detected = detector(
    "./data/cat.jpg",
    candidate_labels=["cat", "dog", "truck", "couch", "remote"],
)

print(detected)

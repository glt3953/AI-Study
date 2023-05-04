import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

image_file = "./data/cat.jpg"
image =  Image.open(image_file)

categories = ["cat", "dog", "truck", "couch"]
categories_text = list(map(lambda x: f"a photo of a {x}", categories))
inputs = processor(text=categories_text, images=image, return_tensors="pt", padding=True)

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)

for i in range(len(categories)):
    print(f"{categories[i]}\t{probs[0][i].item():.2%}")

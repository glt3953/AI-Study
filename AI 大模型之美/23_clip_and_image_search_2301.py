import torch
from PIL import Image
from IPython.display import display
from IPython.display import Image as IPyImage
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_image_feature(filename: str):
    image = Image.open(filename).convert("RGB")
    processed = processor(images=image, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        image_features = model.get_image_features(pixel_values=processed["pixel_values"])
    return image_features

def get_text_feature(text: str):
    processed = processor(text=text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        text_features = model.get_text_features(processed['input_ids'])
    return text_features

def cosine_similarity(tensor1, tensor2):
    tensor1_normalized = tensor1 / tensor1.norm(dim=-1, keepdim=True)
    tensor2_normalized = tensor2 / tensor2.norm(dim=-1, keepdim=True)
    return (tensor1_normalized * tensor2_normalized).sum(dim=-1)

image_tensor = get_image_feature("./data/cat.jpg")

cat_text = "This is a cat."
cat_text_tensor = get_text_feature(cat_text)

dog_text = "This is a dog."
dog_text_tensor = get_text_feature(dog_text)

display(IPyImage(filename='./data/cat.jpg'))

two_cats_text = "There are two cats."
two_cats_text_tensor = get_text_feature(two_cats_text)

truck_text = "This is a truck."
truck_text_tensor = get_text_feature(truck_text)

couch_text = "This is a couch."
couch_text_tensor = get_text_feature(couch_text)

print("Similarity with cat : ", cosine_similarity(image_tensor, cat_text_tensor))
print("Similarity with dog : ", cosine_similarity(image_tensor, dog_text_tensor))
print("Similarity with two cats : ", cosine_similarity(image_tensor, two_cats_text_tensor))
print("Similarity with truck : ", cosine_similarity(image_tensor, truck_text_tensor))
print("Similarity with couch : ", cosine_similarity(image_tensor, couch_text_tensor))

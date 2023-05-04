
from datasets import load_dataset

#dataset = load_dataset("rajuptvs/ecommerce_products_clip")
#dataset = load_dataset("syedashfaq/Motorcycles")
dataset = load_dataset("alexrods/mini_car_bikes_detection")

print(dataset)


import matplotlib.pyplot as plt

training_split = dataset["train"]

def display_images(images):
    fig, axes = plt.subplots(2, 5, figsize=(15, 6))
    axes = axes.ravel()

    for idx, img in enumerate(images):
        axes[idx].imshow(img)
        axes[idx].axis('off')

    plt.subplots_adjust(wspace=0.2, hspace=0.2)
    plt.show()

images = [example["image"] for example in training_split.select(range(10))]
display_images(images)

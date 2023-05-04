
import cv2
from matplotlib import pyplot as plt

# Read the image
image_path = "./data/cat.jpg"
image = cv2.imread(image_path)

# Convert the image from BGR to RGB format
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Draw the bounding box and label for each detected object
for detection in detected:
    box = detection['box']
    label = detection['label']
    score = detection['score']
    
    # Draw the bounding box and label on the image
    xmin, ymin, xmax, ymax = box['xmin'], box['ymin'], box['xmax'], box['ymax']
    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
    cv2.putText(image, f"{label}: {score:.2f}", (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image in Jupyter Notebook
plt.imshow(image)
plt.axis('off')
plt.show()

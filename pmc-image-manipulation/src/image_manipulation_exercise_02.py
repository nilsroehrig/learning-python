import os
import cv2

base_path = "../materials/sample_images"

for filename in os.listdir(base_path):
    image = cv2.imread(f"{base_path}/{filename}")
    resized = cv2.resize(image, (100,100))
    cv2.imwrite(f"{base_path}/resized_{filename}", resized)
import cv2 as cv
import numpy as np
from tkinter import filedialog
import os
import glob

dir_path= filedialog.askdirectory()
paths = []
if dir_path:
        img_paths = []
        for folder in os.listdir(dir_path):
            folder = os.path.join(dir_path, folder)
            files = os.path.join(folder, "*.jpg")
            print(f"Loading {folder}")
            [paths.append(e) for e in glob.glob(files)]
else:
        raise FileNotFoundError

for path in paths:
    img = cv.imread(path)

    target_size = (416, 416)

    # Get the original image dimensions
    original_height, original_width, _ = img.shape

    # Calculate the scaling factors for both dimensions
    width_scale = target_size[0] / original_width
    height_scale = target_size[1] / original_height

    # Determine the scaling factor to maintain the aspect ratio
    scaling_factor = min(width_scale, height_scale)

    # Calculate the new size to maintain the aspect ratio
    new_width = int(original_width * scaling_factor)
    new_height = int(original_height * scaling_factor)

    # Resize the image while maintaining the aspect ratio
    resized_image = cv.resize(img, (new_width, new_height))

    # Create a new image with the target size and paste the resized image in the center
    output_image = np.full((target_size[1], target_size[0], 3), 255, dtype=np.uint8)
    x_offset = (target_size[0] - new_width) // 2
    y_offset = (target_size[1] - new_height) // 2
    output_image[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_image

    cv.imwrite(path, output_image)

print("All images have been converted.")
       
'''

'''

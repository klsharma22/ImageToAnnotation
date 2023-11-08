import cv2
import tkinter as tk
from tkinter import filedialog
import os
import glob

path = '/Users/klsharma22/Desktop/NextGenTechInc/Object Detection/Model/Custom-made/data/gerenuk/image_0032.jpg'

import cv2
import numpy as np

# Read the original image
original_image = cv2.imread(path)

# Calculate the target size (416x416)
target_size = (416, 416)

# Get the original image dimensions
original_height, original_width, _ = original_image.shape

# Calculate the scaling factors for both dimensions
width_scale = target_size[0] / original_width
height_scale = target_size[1] / original_height

# Determine the scaling factor to maintain the aspect ratio
scaling_factor = min(width_scale, height_scale)

# Calculate the new size to maintain the aspect ratio
new_width = int(original_width * scaling_factor)
new_height = int(original_height * scaling_factor)

# Resize the image while maintaining the aspect ratio
resized_image = cv2.resize(original_image, (new_width, new_height))

# Create a new image with the target size and paste the resized image in the center
output_image = np.full((target_size[1], target_size[0], 3), 255, dtype=np.uint8)
x_offset = (target_size[0] - new_width) // 2
y_offset = (target_size[1] - new_height) // 2
output_image[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_image

cv2.imshow('Sample', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
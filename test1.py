import cv2
import tkinter as tk
from tkinter import filedialog

def load_images():
    file_paths = filedialog.askopenfilenames(title="Select Image Files", filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])

    return file_paths

load_images()

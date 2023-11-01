import cv2
import tkinter as tk
from tkinter import filedialog
import os
import glob

def track_files():
    dir_path= filedialog.askdirectory()

    return dir_path

def load_images(dir_path):
    if dir_path:
        img_paths = {}
        for folder in os.listdir(dir_path):
            folder = os.path.join(dir_path, folder)
            files = os.path.join(folder, "*.jpg")
            img_paths.update({folder.split('/')[-1] : glob.glob(files)})

        return img_paths
    else:
        raise FileNotFoundError


directory_path = track_files()

print(load_images(directory_path).keys())
'''
try:
    counter = 0
    for path in file_path_list:
        load_images(path)
        counter += 1

    print(f"{counter} files were loaded.")
except FileNotFoundError:
    print(f"Only {counter} files were loaded.")
    '''

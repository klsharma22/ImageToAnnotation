import cv2
import tkinter as tk
from tkinter import filedialog
import os
import glob

def track_files():
    dir_path= filedialog.askdirectory()

    if dir_path:
        img_paths = {}
        for folder in os.listdir(dir_path):
            folder = os.path.join(dir_path, folder)
            files = os.path.join(folder, "*.jpg")
            img_paths.update({folder.split('/')[-1] : glob.glob(files)})

        return img_paths
    else:
        raise FileNotFoundError

def load_images(file_path):
    for key in file_path.keys():
        for img_path in file_path[key]:
            img = cv2.imread(img_path)
            cv2.imshow(key, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    


image_path = track_files()

print(load_images(image_path))
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

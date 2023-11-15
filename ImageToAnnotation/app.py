import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import logging
import os
import glob
from PIL import Image, ImageTk      
import cv2 as cv
import threading
import time
import numpy as np
import annotation as an


class App:
      def __init__(self, root):
            self.root = root
            logging.basicConfig(filename= 'app.log', filemode= 'w', format=' %(name)s - %(levelname)s - %(message)s')
            self.root.geometry("700x700")

            self.xmin_label, self.xmax_label = ttk.Label(self.root, text= "xmin"), ttk.Label(self.root, text= "xmax")
            self.ymin_label, self.ymax_label = ttk.Label(self.root, text= "ymin"), ttk.Label(self.root, text= "ymax")

            self.xmin_value, self.xmax_value = ttk.Label(self.root, text= "0"), ttk.Label(self.root, text= "0")
            self.ymin_value, self.ymax_value = ttk.Label(self.root, text= "0"), ttk.Label(self.root, text= "0")

            self.load_btn = tk.Button(self.root, text= "Load Image", command= self.track_files)
            self.load_btn.place(relx=0.35, rely= 0.025)
            self.next_btn = tk.Button(self.root, text= "Next", command=self.next_image)
            self.next_btn.place(relx= 0.5, rely= 0.025)

            self.progress_label = tk.Label(self.root, text= "0%")
            self.progress_label.place(relx=0.05, rely=0.9)

            self.name = tk.StringVar()
            self.object_text = ttk.Combobox(self.root, textvariable= self.name)
            self.object_text.set('Select an option')
            self.object_text.place(relx= 0.7, rely=0.1)

            self.save_btn = tk.Button(self.root, text= 'Save', command= self.save)
            self.save_btn.place(relx=0.7, rely=0.2)

            self.saved_status_label = tk.Label(self.root, text= "")
            self.saved_status_label.place(relx= 0.7, rely=0.25)

            self.add_btn = tk.Button(self.root, text= 'Add Boundary', command= self.add_boundary)
            self.add_btn.place(relx=0.7, rely=0.15)

            self.dd = tk.IntVar()
            self.t = tk.IntVar()
            self.o = tk.IntVar()

            self.difficult_detect = tk.Checkbutton(self.root, text= "Difficult", variable= self.dd)
            self.truncated = tk.Checkbutton(self.root, text= "Truncated", variable= self.t)
            self.occluded = tk.Checkbutton(self.root, text= "Occluded", variable= self.o)

            self.difficult_detect.place(relx= 0.7, rely= 0.25)
            self.truncated.place(relx= 0.7, rely= 0.3)
            self.occluded.place(relx=0.7, rely= 0.35)


            if self.xmin_value and self.xmax_value and self.ymin_value and self.ymax_value:
                  logging.info("Labels have been initiated successfully.")
            else:
                  logging.error("Labels have not been initiated successfully.")

            self.xmin_label.place(relx=0.15, rely=0.025)
            self.xmax_label.place(relx=0.25, rely=0.025)
            self.ymin_label.place(relx=0.15, rely=0.05)
            self.ymax_label.place(relx=0.25, rely=0.05)

            self.xmin_value.place(relx=0.2, rely=0.025)
            self.xmax_value.place(relx=0.3, rely=0.025)
            self.ymin_value.place(relx=0.2, rely=0.05)
            self.ymax_value.place(relx=0.3, rely=0.05)

            self.canvas = tk.Canvas(self.root, width= 416, height= 416, bg= "white")
            self.canvas.place(relx=0.05, rely=0.1)

            self.canvas.bind('<Button-1>', self.mouse_init)
            self.canvas.bind('<B1-Motion>', self.create_box)

            self.start_pos = None
            self.final_pos = None
            self.current_box = None
            self.current_image = None
            self.file_path_list = []
            self.image = []
            self.index = 0
            self.objects = []
            self.object_name_list = []
            self.image_loading_complete = threading.Event()


      def add_boundary(self):
            object_dict = {'name': self.object_text.get(),
                           'bnd_dim': [self.start_pos[0], self.start_pos[1], self.final_pos[0], self.final_pos[1]],
                           'check_box': [self.dd.get(), self.t.get(), self.o.get()]}
            self.objects.append(object_dict)
            self.reset()

      def reset(self):
            self.canvas.delete(self.current_box)
            self.current_box = None
            self.start_pos = None
            self.final_pos = None
            self.object_text.set('Select an option')
            pass

      def save(self):
            an.create_annotation(self.file_path_list[self.index], 
                                 self.objects)
            self.saved_status_label.config(text= 'Saved')
            self.objects = []


      def mouse_init(self, event):
            self.start_pos = (event.x, event.y)
            self.xmin_value.config(text= f"{self.start_pos[0]}")
            self.ymin_value.config(text= f"{self.start_pos[1]}")

      def create_box(self, event):
            self.final_pos = (event.x, event.y)
            self.xmax_value.config(text=f"{self.final_pos[0]}")
            self.ymax_value.config(text= f"{self.final_pos[1]}")
            if self.start_pos:
                  if self.current_box:
                        self.canvas.delete(self.current_box)
                  self.current_box = self.canvas.create_rectangle(
                        self.start_pos[0], self.start_pos[1], self.final_pos[0], self.final_pos[1], outline= 'red'
                  )
            self.root.update_idletasks()

      def load_images(self):
            for i, f in enumerate(self.file_path_list):
                  img = cv.imread(f)
                  img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                  img = Image.fromarray(img)
                  img = ImageTk.PhotoImage(img)
                  self.image.append(img)

                  value = (i + 1) * 100 / len(self.file_path_list)
                  if value == 100:
                        self.progress_label.config(text= "Completed")
                  else:
                        self.progress_label.config(text=f"{round(value, 2)}%")
                  self.root.update_idletasks()

            self.image_loading_complete.set()
            print(len(self.image))
            self.root.after(0, self.next_btn.config(state= 'active'))

      def track_files(self):
            dir_path= filedialog.askdirectory()

            if dir_path:
                  img_paths = []
                  for folder in os.listdir(dir_path):
                        self.object_name_list.append(folder)
                        folder = os.path.join(dir_path, folder)
                        files = os.path.join(folder, "*.jpg")
                        print(f"Loading {folder}")
                        [self.file_path_list.append(e) for e in glob.glob(files)]    
                  self.next_btn.config(state= 'disabled')
                  self.object_text['values'] = tuple(self.object_name_list)
                  threading.Thread(target= self.load_images).start()
                  self.image_loading_complete.clear()
                  self.root.update_idletasks()
            else:
                  raise FileNotFoundError

      def next_image(self):
            self.image_loading_complete.wait()
            self.saved_status_label.config(text=" ")
            self.difficult_detect.deselect()
            self.truncated.deselect()
            self.occluded.deselect()

            if self.index < len(self.image):
                  if self.current_image:
                        self.canvas.delete("image")
                  self.current_image = self.image[self.index]
                  self.canvas.create_image(209, 209, image= self.current_image, tag= "image")
                  self.index += 1
            

            

if __name__ == '__main__':
      root = tk.Tk()
      app = App(root)
      root.mainloop()

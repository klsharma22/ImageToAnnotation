import tkinter as tk
from tkinter import ttk
import logging

class App:
      def __init__(self, root):
            self.root = root
            logging.basicConfig(filename= 'app.log', filemode= 'w', format=' %(name)s - %(levelname)s - %(message)s')
            self.root.geometry("1000x1000")

            self.xmin_label, self.xmax_label = ttk.Label(self.root, text= "xmin"), ttk.Label(self.root, text= "xmax")
            self.ymin_label, self.ymax_label = ttk.Label(self.root, text= "ymin"), ttk.Label(self.root, text= "ymax")

            self.xmin_value, self.xmax_value = ttk.Label(self.root, text= "0"), ttk.Label(self.root, text= "0")
            self.ymin_value, self.ymax_value = ttk.Label(self.root, text= "0"), ttk.Label(self.root, text= "0")

            self.load_btn = tk.Button(self.root, text= "Load Image", command= self.load_image)

            if self.xmin_value and self.xmax_value and self.ymin_value and self.ymax_value:
                  logging.info("Labels have been initiated successfully.")
            else:
                  logging.error("Labels have not been initiated successfully.")

            self.xmin_label.place(relx=0.15, rely=0.025)
            self.xmax_label.place(relx=0.25, rely=0.025)
            self.ymin_label.place(relx=0.15, rely=0.045)
            self.ymax_label.place(relx=0.25, rely=0.045)

            self.xmin_value.place(relx=0.2, rely=0.025)
            self.xmax_value.place(relx=0.3, rely=0.025)
            self.ymin_value.place(relx=0.2, rely=0.045)
            self.ymax_value.place(relx=0.3, rely=0.045)

            self.canvas = tk.Canvas(self.root, width= 900, height= 700, bg= "white")
            self.canvas.place(relx=0.05, rely=0.1)

            self.canvas.bind('<Button-1>', self.mouse_init)
            self.canvas.bind('<B1-Motion>', self.create_box)

            self.start_pos = None
            self.final_pos = None
            self.current_box = None

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

      def load_image(self):
            pass
      




if __name__ == '__main__':
      root = tk.Tk()
      app = App(root)
      root.mainloop()
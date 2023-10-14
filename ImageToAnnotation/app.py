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

            if self.xmin_label and self.xmax_label and self.ymin_label and self.ymax_label:
                  logging.info("Labels have been initiated successfully.")
            else:
                  logging.error("Labels have not been initiated successfully.")

            self.xmin_label.place(relx=0.05, rely=0.025)
            self.xmax_label.place(relx=0.25, rely=0.025)
            self.ymin_label.place(relx=0.05, rely=0.125)
            self.ymax_label.place(relx=0.25, rely=0.125)

            frame = tk.Frame(self.root, width= 500, height= 500)
            frame.place(relx=0.05, rely=0.2)

            frame.bind('<Motion>', self.mouse_coordinate)

      def mouse_coordinate(self, event):
            self.xmin_label.config(text= f"{event.x}")
            self.ymin_label.config(text= f"{event.y}")



if __name__ == '__main__':
      root = tk.Tk()
      app = App(root)
      root.mainloop()
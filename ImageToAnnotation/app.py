import tkinter as tk
from tkinter import ttk
import logging

class App(tk.Tk):
    def __init__(self):
            super().__init__()
            logging.basicConfig(filename= 'app.log', filemode= 'w', format=' %(name)s - %(levelname)s - %(message)s')
            self.geometry("300x300")
            xmin_label, xmax_label = ttk.Label(self, text= "xmin"), ttk.Label(self, text= "xmax")
            ymin_label, ymax_label = ttk.Label(self, text= "ymin"), ttk.Label(self, text= "ymax")

            if xmin_label and xmax_label and ymin_label and ymax_label:
                  logging.info("Labels have been initiated successfully.")
            else:
                  logging.error("Labels have not been initiated successfully.")

            xmin_label.place(relx=0.2, rely=0.1)
            xmax_label.place(relx=0.66, rely=0.1)
            ymin_label.place(relx=0.2, rely= 0.4)
            ymax_label.place(relx=0.66, rely=0.4)


app = App()
app.mainloop()
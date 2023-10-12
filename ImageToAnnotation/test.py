import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class BoundingBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bounding Box Annotation Tool")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.canvas.bind("<Button-1>", self.start_bbox)
        self.canvas.bind("<B1-Motion>", self.draw_bbox)

        self.bbox_start = None
        self.bbox_end = None
        self.current_bbox = None
        self.image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0.5, 0.5, anchor="center", image=self.image)

    def start_bbox(self, event):
        self.bbox_start = (event.x, event.y)

    def draw_bbox(self, event):
        if self.bbox_start:
            if self.current_bbox:
                self.canvas.delete(self.current_bbox)
            self.bbox_end = (event.x, event.y)
            self.current_bbox = self.canvas.create_rectangle(
                self.bbox_start[0], self.bbox_start[1], self.bbox_end[0], self.bbox_end[1], outline="red"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = BoundingBoxApp(root)
    root.mainloop()

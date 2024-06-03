
import cv2
import numpy as np
import pandas as pd
from collections import Counter 
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

from ultralytics import YOLO

class ObjectDetectorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Object Detector")

        self.select_button = tk.Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.model = YOLO("best1.pt")
        self.class_list = ['tree']

    def select_image(self):
        path = filedialog.askopenfilename()
        if path:
            object_classes, im_rgb = self.detect_objects(path)
            self.display_results(object_classes, im_rgb)

    def detect_objects(self, path):
        results = self.model.predict(path)
        a = results[0].boxes.data
        px = pd.DataFrame(a).astype("float")
        object_classes = []

        for index, row in px.iterrows():
            d = int(row[5])
            obj_class = self.class_list[d]
            object_classes.append(obj_class)

        counter = Counter(object_classes)
        object_count_text = "\n".join([f"{obj} count : {count}" for obj, count in counter.items()])

        return object_count_text, results[0].plot()

    def display_results(self, object_count_text, im_rgb):
        self.result_label.config(text=object_count_text)
        im_rgb_pil = Image.fromarray(im_rgb.astype('uint8'))
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        im_rgb_pil_resized = im_rgb_pil.resize((canvas_width, canvas_height))
        im = ImageTk.PhotoImage(im_rgb_pil_resized)
        self.canvas.image = im
        self.canvas.create_image(0, 0, anchor='nw', image=im)



def main():
    root = tk.Tk()
    root.geometry("800x600")
    gui = ObjectDetectorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
import time
import numpy as np
import random

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.f = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position

class App:
    def __init__(self, canvas_height=800, canvas_width=800, side_length=16):
        self.root = tk.Tk()
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.start_point = self.end_point = None
        self.rows = self.canvas_height // side_length
        self.cols = self.canvas_width // side_length
        self.maze = np.zeros((self.rows, self.cols))
        self.visStarted = False

        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.side_length = side_length
        self.grid()

    def start(self):
        self.root.title('A* Algorithm Path Visualiser')
        self.root.geometry(f"{self.canvas_height}x{self.canvas_width + 100}")

        self.text_box = tk.Label(self.root, text="Select starting point")
        self.text_box.config(font=("Courier", 14), bg="white")
        self.text_box.pack(side=tk.TOP, anchor=tk.CENTER)

        sbtn = tk.Button(self.root, text="Start", command=self.find_path)
        sbtn.place(x=self.canvas_height * 0.40, y=self.canvas_width + 70, anchor=tk.CENTER)

        rbtn = tk.Button(self.root, text="Reset all", command=self.reset)
        rbtn.place(x=self.canvas_height * 0.60, y=self.canvas_width + 70, anchor=tk.CENTER)

        self.canvas.place(x=0, y=50)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<Button-1>', self.draw)
        self.root.bind("<space>", self.find_path)
        self.root.mainloop()

    def grid(self, obstacle_density=0.2):
        pad = self.side_length // 2
        self.canvas.create_rectangle(-pad, -pad, pad, pad, fill="black", outline="grey")

        for i in range(pad, self.canvas_height, self.side_length):
            for j in range(pad, self.canvas_width, self.side_length):
                if random.random() < obstacle_density:
                    self.maze[i // self.side_length][j // self.side_length] = 1
                    self.canvas.create_rectangle(i - pad, j - pad, i + pad, j + pad, fill="black", outline="grey")
                else:
                    self.canvas.create_rectangle(i - pad, j - pad, i + pad, j + pad, fill="white", outline="grey")

    def reset(self, obstacle_density=0.2):
        self.visStarted = False
        self.maze = np.zeros((self.rows, self.cols))
        self.canvas.delete("all")
        self.grid(obstacle_density)
        self.start_point = self.end_point = None
        self.show_text("Select starting point")

    def show_text(self, text, text_color="black"):
        self.text_box.config(text=text, fg=text_color)

    def get_pos(self, side_length, coordinates):
        x = coordinates[0] // side_length
        y = coordinates[1] // side_length
        return x, y

    def draw(self, event):
        if self.visStarted == True:
            return

        pos = self.get_pos(self.side_length, (event.x, event.y))

        if pos == None:
            return
        else:
            xa, ya = pos

        if not self.start_point:
            self.start_point = Node(None, (xa, ya))
            color = "orange"
        elif not self.end_point:
            self.end_point = Node(None, (xa, ya))
            color = "cyan"
        elif self.maze[xa][ya] != 1:
            self.maze[xa][ya] = 1
            color = "black"
        else:
            return

        self.canvas.create_rectangle(xa * self.side_length - self.side_length // 2, ya * self.side_length - self.side_length // 2,
                                     xa * self.side_length + self.side_length // 2, ya * self.side_length + self.side_length // 2,
                                     fill=color, outline="grey")
        if self.start_point and self.end_point:
            self.show_text("Press 'Space' to start A* algorithm", "green")

    def find_path(self, event=None):
        if self.start_point and self.end_point:
            self.Astar()
        elif self.start_point:
            self.show_text("Select destination point", "red")
        else:
            self.show_text("Select starting point", "red")

    def Astar(self):
        self.show_text("A* Algorithm running")
        self.visStarted = True
        # Implement A* algorithm here

def main():
    app = App(800, 800, 16)
    app.start()

if __name__ == '__main__':
    main()

from tkinter import *
from tkinter import ttk


class Labels(ttk.Label):
    def __init__(self, text, size_x, size_y, color):
        super().__init__(text=text)
        self.text = text
        self.rel_x = size_x
        self.rel_y = size_y
        self.bg = color

    def inspect_label(self):
        self["text"] = self.text
        self.pack()

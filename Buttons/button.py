from tkinter import *
from tkinter import ttk


class Buttons(ttk.Button):
    def __init__(self, text, size_x, size_y, color):
        super().__init__(text=text)
        self.text = text
        self.rel_x = size_x
        self.rel_y = size_y
        self.bg = color

    def inspect_button(self):
        self["text"] = self.text
        self.pack()



from tkinter import *
from tkinter import ttk
from Buttons import button
from Labels import label
import LOGOS

root = Tk()  # создаем корневой объект - окно

root.title("Приложение для решения задания 2 по КСЕ")  # устанавливаем заголовок окна
root.geometry("600x400+150+90")  # устанавливаем размеры окна
# root.iconbitmap(default="LOGOS\logo.ico") # не робит потому что пидарас

b_1 = button.Buttons(text="123", size_x=123, size_y=123, color="red")
b_1.inspect_button()

l_1 = label.Labels(text="123", size_x=123, size_y=123, color="red")
l_1.inspect_label()

root.mainloop()

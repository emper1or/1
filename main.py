from tkinter import *

from Buttons import button
from Labels import label


root = Tk()  # создаем корневой объект - окно

root.title("Приложение для решения задания 2 по КСЕ")  # устанавливаем заголовок окна
root.geometry("600x400+150+90")  # устанавливаем размеры окна
#root.attributes("-fullscreen", True)
root.iconbitmap(default="LOGOS\logo.ico")




b_1 = button.Buttons("123", 123, 123, "red")
b_1.inspect_button()

l_1 = label.Labels("123", 123, 123, "red")
l_1.inspect_label()


root.mainloop()
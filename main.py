from tkinter import *
from tkinter import ttk

root = Tk()  # создаем корневой объект - окно

root.title("Приложение для решения задания 2 по КСЕ")  # устанавливаем заголовок окна
root.geometry("600x400+150+90")  # устанавливаем размеры окна
root.iconbitmap(default="LOGOS\logo.ico")  # не робит потому что пидарас


def close_window(window):
    close_button = ttk.Button(window, text="Закрыть окно", command=lambda: window.destroy())
    close_button.pack(anchor="center", expand=1)


def first_click(text, res):
    window = Tk()
    window.title(text)
    window.geometry(res)
    close_window(window)


b_1 = Button(text="First button", command=lambda: first_click(text="New Win", res="600x400"))
b_1.pack(anchor=CENTER, expand=1)

b_2 = Button()

# l_1 = label.Labels(text="123", size_x=123, size_y=123, color="red")
# l_1.inspect_label()

root.mainloop()

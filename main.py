from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()  # создаем корневой объект - окно

root.title("GIIK's")  # устанавливаем заголовок окна
root.geometry("300x300+150+90")  # устанавливаем размеры окна
root.iconbitmap(default="LOGOS\logo.ico")  # не робит потому что пидарас
root.config(background='#E2F1F1')  # установка цвета
root.resizable(False, False)


# функция для создания окон с кнопкой закрытия
def exit_buttons(window):
    exit_button = Button(window, text="EXIT", bg="#C5F4F4", command=lambda: window.destroy())
    exit_button.pack(anchor=SE, expand=1, padx=20, pady=20)


def first_click(text, res):
    window = Tk()
    window.title(text)
    window.geometry(res)
    window.config(bg="#E2F1F1")
    window.resizable(False, False)
    exit_buttons(window)


def input_base(text, res):
    window = Tk()

    window.title(text)
    window.geometry(res)
    window.config(bg="#E2F1F1")
    window.resizable(False, False)

    label_of_input = Label(window, text="Задача № 2.3", bg="#E2F1F1")
    label_of_input.pack(anchor=N, expand=1)

    text_of_text = f"Механизм (рис. 2.3) состоит из двух блоков 2 и 3, каждый из которых \
                    \nобразован совокупностью жестко связанных большого и малого цилиндров. \
                    \nМалый цилиндр 2 взаимодействует (без скольжения) с большим цилиндром 3 в\
                    \nточке В. Большой цилиндр 2 НЕ взаимодействует с малым цилиндром 3. К \
                    \nбольшому цилиндру 2 в точке А на «нерастяжимом тросе» подвешен груз 1, \
                    \nкоторый совершает «прямолинейное движение» по заданному уравнению. \
                    \nОпределить «путь», пройденный грузом 1, а так же «скорость», «нормальное», \
                    \n«тангенциальное» и «полное ускорение» точки М малого цилиндра блока 3 \
                    \nмеханизма в момент времени t ."

    text_label_of_input = Label(window, text=text_of_text, bg="#E2F1F1")
    text_label_of_input.pack(anchor=N, expand=1)
    #сюда надо картинку

    exit_buttons(window)


l_1 = Label(text="Приложение для решения задания 2 по КСЕ", bg="#E2F1F1")
l_1.pack(anchor='center', expand=1, fill=X)

b_1 = Button(text="Условия", bg="#C5F4F4", command=lambda: input_base(text="Условия", res="600x400"))

b_1.pack(anchor='center', expand=1)

b_2 = Button(text="Переменные условия", bg="#C5F4F4",
             command=lambda: first_click(text="Введите параметры", res="600x400"))
b_2.pack(anchor='center', expand=1)

b_3 = Button(text="Решение", bg="#C5F4F4", command=lambda: first_click(text="Решение", res="600x400"))
b_3.pack(anchor='center', expand=1)

exit_buttons(root)

root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
# import matplotlib.pyplot as plt
import math

root = Tk()  # создаем корневой объект - окно

root.title("GIIK's")  # устанавливаем заголовок окна
root.geometry("300x300+150+90")  # устанавливаем размеры окна
root.iconbitmap("logo.ico")  # не робит потому что пидарас
root.config(background='#E2F1F1')  # установка цвета
root.resizable(False, False)

t = 22


def input_base(text, res):
    window = Toplevel()

    window.title(text)
    window.geometry(res)
    window.config(bg="#E2F1F1")
    window.resizable(False, False)

    first_button(window)
    second_button(window)


def input_base_t(text, res):
    window = Toplevel()

    window.title(text)
    window.geometry(res)
    window.config(bg="#E2F1F1")
    window.resizable(False, False)

    second_button(window)


def answer_base(text, res):
    window = Toplevel()

    window.title(text)
    window.geometry(res)
    window.config(bg="#E2F1F1")
    window.resizable(False, False)

    answer_button(window)


def first_button(window):
    window.iconbitmap("logo.ico")
    label_of_input = Label(window, text="Задача № 2.3", bg="#E2F1F1")
    label_of_input.pack(anchor=N)

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
    text_label_of_input.pack(fill=X)
    # сюда надо картинку
    image1 = Image.open("struckture_scheme.png")
    image1 = image1.resize((400, 300))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(window, image=test)
    label1.image = test
    # Position image
    label1.place(x=100, y=180)

    exit_buttons(window)

    window.mainloop()


def second_button(window):
    window.iconbitmap("logo.ico")

    def show_message():
        if entry.get().isnumeric():
            global t
            label["text"] = f'Вы успешно изменили переменную t: {entry.get()}'
            t = int(entry.get())
        else:
            label["text"] = f"Введите корректное время!"

    label_of_input = Label(window, text="Введите переменную t в секундах (с)", bg="#E2F1F1")
    label_of_input.pack(anchor=N)

    entry = Entry(window)
    entry.insert(0, "22")
    entry.pack(padx=10, pady=4)

    btn = Button(window, text="Добавить время", command=show_message)
    btn.pack(anchor=N, padx=6, pady=6)

    label = Label(window)
    label.pack(anchor=N, padx=6, pady=6)

    '''
    image2 = Image.open("filename.png")
    os.remove("C:/Users/emper1or/Desktop/КСЕ/KCE projeckt 1/filename.png")
    image2.crop((100,100, 100, 100)).save("filename.png", quality=95)
    image1 = Image.open("filename.png")
    image1 = image1.resize((192, 144))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(window, image=test)
    label1.image = test
    # Position image
    label1.place(x=100, y=78)'''

    exit_buttons(window)

    window.mainloop()


def answer_button(window):
    window.iconbitmap("logo.ico")
    label_of_answer = Label(window, text="Решение задачи", bg="#E2F1F1")
    label_of_answer.pack(anchor=N)

    global t
    s_1 = 32 + 125 * t ** 2
    v_1 = 250 * t / 1000

    at_1 = 0.25

    w2 = v_1 / (100 * 10 ** (-3))
    e2 = at_1 / (100 * 10 ** (-3))

    vb = w2 * 72 * 10 ** (-3)
    atb = e2 * 72 * 10 ** (-3)

    w3 = vb / (150 * 10 ** (-3))
    e3 = atb / (150 * 10 ** (-3))

    vm = w3 * 130 * 10 ** (-3)
    atm = e3 * 130 * 10 ** (-3)

    anm = round(vm ** 2 / (130 * 10 ** (-3)), 1)
    am = round(math.sqrt(anm ** 2 + atm ** 2), 5)
    text_of_answer = (
        f"Ответ: в момент времени t = {t} с груз прошел «путь» равный {s_1}мм, \n а точка М малого цилиндра "
        f"блока 3 механизма имеет \n «нормальное ускорение» {anm}м/c^2,\n«тангенциальное ускорение» {atm}м/c^2 и "
        f"«полное ускорение» {am}м/c^2")

    text_label_of_input = Label(window, text=text_of_answer, bg="#E2F1F1")
    text_label_of_input.pack(fill=X)

    exit_buttons(window)

    window.mainloop()


def exit_buttons(window):
    exit_button = Button(window, text="EXIT", bg="#C5F4F4", command=lambda: window.destroy())
    exit_button.pack(anchor=SE, expand=1, padx=20, pady=20)


l_1 = Label(text="Приложение для решения задания 2 по КСЕ", bg="#E2F1F1")
l_1.pack(anchor='center', expand=1)

b_1 = Button(text="Условия", bg="#C5F4F4", command=lambda: input_base(text="Условия", res="600x500"))
b_1.pack(anchor='center', expand=1)

b_2 = Button(text="Переменные условия", bg="#C5F4F4",
             command=lambda: input_base_t(text="Введите параметры", res="300x300"))
b_2.pack(anchor='center', expand=1)

b_3 = Button(text="Решение", bg="#C5F4F4", command=lambda: answer_base(text="Решение", res="600x150"))
b_3.pack(anchor='center', expand=1)

exit_buttons(root)

root.mainloop()

import math
from tkinter import Tk, Label, Entry, Button

def click_button():
    n = int(entry.get())

    if n <= 0:
        show_message("Введите n > 0!")
    else:
        window.destroy()
        create_function_input_window(n)

def create_function_input_window(n):
    window1 = Tk()
    window1.title("Анализ функций")

    Label(window1, text="Анализ функций", font=("Arial", 20)).pack()

    for i in range(n):
        Label(window1, text=f'Введите функцию {i + 1}:', font=("Arial", 12)).pack()
        entry_function = Entry(window1)
        entry_function.pack()
        functions.append(entry_function)

    Button(window1, text="Ввести", command=lambda: process_functions(functions)).pack()

def process_functions(entries):
    function_values = [entry.get() for entry in entries]

    if not all(is_binary_function(f) for f in function_values):
        show_message("Введены некорректные значения функций.")
        return

    analyze_functions(function_values)

def is_binary_function(function):
    return all(c in ['0', '1'] for c in function)

def analyze_functions(functions):
    Sam, T0, T1, M, L = [], [], [], [], []

    for function in functions:
        Sam.append(check_self_duality(function))
        T0.append(check_zero_preserving(function))
        T1.append(check_one_preserving(function))
        M.append(check_monotonicity(function))
        L.append(check_linearity(function))

    is_full_set = all(check_completeness(cl) for cl in [Sam, T0, T1, M, L])
    show_message(f"Набор {'полный' if is_full_set else 'неполный'}")

    for i, function in enumerate(functions):
        class_msg = f'Функция {i + 1}: Sam={Sam[i]}, T0={T0[i]}, T1={T1[i]}, Monotone={M[i]}, Линейность={L[i]}'
        show_message(class_msg)

def check_self_duality(function):
    half_len = len(function) // 2
    return all(int(function[i]) + int(function[-(i + 1)]) == 1 for i in range(half_len))

def check_zero_preserving(function):
    return int(function[0]) == 0

def check_one_preserving(function):
    return int(function[-1]) == 1

def check_monotonicity(function):
    d = int(math.log(len(function), 2))
    for i in range(len(function) - 1):
        for j in range(i + 1, len(function)):
            if (i & j) == i and int(function[i]) > int(function[j]):
                return False
    return True

def check_linearity(function):
    for i in range(len(function)):
        if int(function[i]) == 1:
            if sum(map(int, bin(i)[2:])) > 1:
                return False
    return True

def check_completeness(class_list):
    return all(x == 1 for x in class_list)

def show_message(message):
    window_message = Tk()
    window_message.title("Сообщение")
    Label(window_message, text=message, width=80, height=5, font=("Arial", 12)).pack()

functions = []

window = Tk()
window.title("Анализ функций")
Label(window, text="Введите количество функций:", font=("Arial", 16)).pack()
entry = Entry(window, font=("Arial", 14))
entry.pack()
Button(window, text="Ввести", command=click_button).pack()

window.mainloop()

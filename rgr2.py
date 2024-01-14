import re
from math import *


def is_valid_input_main(a):# метод для проверки и преобразования ввода пользователя в полином
    if re.findall("^(.*[+-].*)$", a) == [a, ]:#проверяем, соответствует ли ввод заданному шаблону
        if a[1] == "-":
            f = -1#если второй символ - , то присваеваем значение -1, иначе 1
        else:
            f = 1
        if "-" in a[2:]:#если есть -, то разбиваем строку и присваиваем -
            a = a[1:-1].split("-")
            g = -1
        else:
            a = a[1:-1].split("+")
            g = 1
        s = [to_list(a[0], f), to_list(a[1], g)]#преобразуем в список
        return s
    else:
        return "Неверный формат ввода, попробуйте ещё раз"


def to_list(a, b):#преобразование в структуру данных, представляющую слагаемое полинома
    bykovki = 0
    ew = 0
    f = 0
    if "i" in a:#для комплексных чисел, если есть комплексная часть, заменяем ее на флаг
        a = a.replace("i", '')
        ew = 1
    for i in a:#считаем буквы
        if i.isalpha():
            bykovki += 1
            if i == "i":
                bykovki -= 1
                f = 1
    if bykovki == 1 and a.strip("\n ")[-1].isalpha() and len(a.strip("-\n ")) > 1:#если буква и она не в конце строки, учтем коэффициент и переменную
        return [float(a.strip("\n ")[:-1].replace(',', ".", 1)) * b, a.strip("\n ")[-1 - f] + "i" * ew]
    elif len(a.strip("-\n ")) == 1 and bykovki == 1:#если буква и она в конце строки, учитываем только переменную
        return [1 * b, a.strip("-\n ") + "i" * ew]


def is_valid_int(u):#проверка на целочисленность строки
    for i in u:
        if i.isdigit():
            pass
        else:
            return "Необходимо число"
    return int(u)


def C_k_n(k, n):#вычисление биномиального коэффициента
    return (factorial(n)) / (factorial(k) * factorial(n - k))


count = 0#для подсчета слагаемых
while True:
    popugai = []#массив для хранения слагаемых полинома
    d = dict()#массив для хранения суммарных значений слагаемых
    stroka_strochenbka = input()#ввод строки полинома
    s = is_valid_input_main(stroka_strochenbka)
    while is_valid_input_main(stroka_strochenbka) == "Неверный формат ввода, попробуйте ещё раз":#запрашиваем данные, пока не будет верного формата
        print(s)
        stroka_strochenbka = input()
        s = is_valid_input_main(stroka_strochenbka)
    number = input()#ввод целого числа
    a = is_valid_int(number)
    while is_valid_int(number) == "Необходимо число":#повторяем, пока не будет введено число
        print(a)
        number = input()
        a = is_valid_int(number)
    ZABbl_DLYA_CHEGO = ""
    billy_sum = 0
    for i in range(a + 1):#цикл для раскрытия полинома по биноминомиальной теореме
        x = a - i
        y = i
        z = C_k_n(y, a)
        chislo = s[0][0] ** x * s[1][0] ** y * z
        if int(chislo) == chislo:
            chislo = int(chislo)
        stroka = s[0][1] * x + s[1][1] * y
        if s[0][1] == s[1][1]:#проверка на совпадение переменных в слагаемых
            billy = 1
        else:
            billy = 0
        how_many_i = 0
        while stroka.count("i") >= 2:
            stroka = stroka.replace("i", '', 2)
            how_many_i += 2
        if how_many_i % 4 == 0:#пересчитываем коэффициенты в зависимости от i
            pass
        else:
            chislo *= -1
        popugai.append(["".join(sorted(stroka)), chislo])
        d["".join(sorted(stroka))] = d.get("".join(sorted(stroka)), 0)+chislo
    for i in d.keys():#выводим раскрытый полином
        if d[i] == 1:
            print(i if count == 0 else "+ " + i, end=' ')
            count += 1
        elif d[i] == 0:
            print('', end='')
        elif d[i] == -1:
            print("-" + i if count == 0 else "- " + i, end=' ')
            count += 1
        elif d[i] < 0 and d[i] != -1:
            print(str(d[i]) + i if count == 0 else "- " + str(abs(d[i])) + i, end=' ')
            count += 1
        else:
            print(str(d[i]) + i if count == 0 else "+ " + str(d[i]) + i, end=' ')
            count += 1
    print("")
    count = 0
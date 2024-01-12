import re
from math import *


def is_valid_input_main(a):
    if re.findall("^(.*[+-].*)$", a) == [a, ]:
        if a[1] == "-":
            f = -1
        else:
            f = 1
        if "-" in a[2:]:
            a = a[1:-1].split("-")
            g = -1
        else:
            a = a[1:-1].split("+")
            g = 1
        s = [to_list(a[0], f), to_list(a[1], g)]
        return s
    else:
        return "Неверный формат ввода, попробуйте ещё раз"


def to_list(a, b):
    bykovki = 0
    ew = 0
    f = 0
    if "i" in a:
        a = a.replace("i", '')
        ew = 1
    for i in a:
        if i.isalpha():
            bykovki += 1
            if i == "i":
                bykovki -= 1
                f = 1
    if bykovki == 1 and a.strip("\n ")[-1].isalpha() and len(a.strip("-\n ")) > 1:
        return [float(a.strip("\n ")[:-1].replace(',', ".", 1)) * b, a.strip("\n ")[-1 - f] + "i" * ew]
    elif len(a.strip("-\n ")) == 1 and bykovki == 1:
        return [1 * b, a.strip("-\n ") + "i" * ew]


def is_valid_int(u):
    for i in u:
        if i.isdigit():
            pass
        else:
            return "Необходимо число"
    return int(u)


def C_k_n(k, n):
    return (factorial(n)) / (factorial(k) * factorial(n - k))


count = 0
while True:
    popugai = []
    d = dict()
    stroka_strochenbka = input()
    s = is_valid_input_main(stroka_strochenbka)
    while is_valid_input_main(stroka_strochenbka) == "Неверный формат ввода, попробуйте ещё раз":
        print(s)
        stroka_strochenbka = input()
        s = is_valid_input_main(stroka_strochenbka)
    number = input()
    a = is_valid_int(number)
    while is_valid_int(number) == "Необходимо число":
        print(a)
        number = input()
        a = is_valid_int(number)
    ZABbl_DLYA_CHEGO = ""
    billy_sum = 0
    for i in range(a + 1):
        x = a - i
        y = i
        z = C_k_n(y, a)
        chislo = s[0][0] ** x * s[1][0] ** y * z
        if int(chislo) == chislo:
            chislo = int(chislo)
        stroka = s[0][1] * x + s[1][1] * y
        if s[0][1] == s[1][1]:
            billy = 1
        else:
            billy = 0
        how_many_i = 0
        while stroka.count("i") >= 2:
            stroka = stroka.replace("i", '', 2)
            how_many_i += 2
        if how_many_i % 4 == 0:
            pass
        else:
            chislo *= -1
        popugai.append(["".join(sorted(stroka)), chislo])
        d["".join(sorted(stroka))] = d.get("".join(sorted(stroka)), 0)+chislo
    for i in d.keys():
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

def check1(l): #проверяем константу 0, при выводе 1 значит, что функция не принадлежит классу поста
    if l[0] == 1:
        return 1
    else:
        return 0
def check2(l): #проверяем константу 1
    if l[-1] == 0:
        return 1
    else:
        return 0

def check(x, y): #сравнение векторов для монотонности
    for i in range(len(str(x))):
        if int(x[i]) < int(y[i]):
            return False
    return True

def check3(l): #проверка на монотонность
    table = []
    m = len(l)
    k = 0
    while m != 1:
        m/=2
        k+=1
    for i in range(len(l)):
        a = bin(i)[2:]
        if len(a) != k:
            a = (k-len(a))*"0" + a
        table.append(a)
    for i in range(len(l)):
        for j in range(len(l)):
            if check(table[i], table[j]):
                if l[i] < l[j]:
                    return 1
    return 0

def check4(l): #проверка на самодвойственность
    m = int(len(l)/2)
    l1 = l[0:m]
    l2 = l[m:len(l)]
    for i in range(len(l1)):
        if l1[i] == l2[len(l2)-1-i]:
            return 1
    return 0

def check5(l): #проверка на линейность
    b = l
    test  = []
    table = []
    m = len(l)
    k = 0
    while m != 1:
        m /= 2
        k += 1
    for i in range(len(l)):
        a = bin(i)[2:]
        if len(a) != k:
            a = (k - len(a)) * "0" + a
        table.append(a)
    for i in range(1, len(l)):
        if i == len(l) - 1:
            if b[0] + b[1] == 1:
                return 1
        else:
            for j in range(1, len(b)):
                if b[j] + b[j - 1] == 0 or b[j] + b[j - 1] == 2:
                    test.append(0)
                else:
                    test.append(1)
            if test[0] == 1:
                if str(table[i]).count('1') > 1:
                    return 1
            b = test
            test = []
    return 0

numbers = int(input('Введите целое положительное число функций для проверки')) #ввод количества функций
while numbers <= 0:
    numbers = int(input('Введите целое положительное число функций для проверки'))

T = [0, 0, 0, 0, 0] #проверка классов поста
for i in range(numbers):
    c = input("Введите функцию")
    g = len(c)
    ost = 0
    while g > 1:
        if ost == 0:
            ost = g % 2
        g //= g
    while ost != 0 or len(c) != c.count('0') + c.count('1') or len(c) == 1 or len(c) == 0:
        print("Неверный ввод функции")
        c = input("Введите функцию")
        g = len(c)
        ost = 0
        while g > 1:
            if ost == 0:
                ost = g % 2
            g //= g
    end = []
    for j in range(len(c)):
        end.append(int(c[j]))
    if T[0] == 0:
        if check1(end) == 1:
            T[0] = 1
    if T[1] == 0:
        if check2(end) == 1:
            T[1] = 1
    if T[2] == 0:
        if check3(end) == 1:
            T[2] = 1
    if T[3] == 0:
        if check4(end) == 1:
            T[3] = 1
    if T[4] == 0:
        if check5(end) == 1:
            T[4] = 1

    if i == (numbers - 1): #красивый вывод
        print("T0", T[0])
        print("T1", T[1])
        print("M", T[2])
        print("S", T[3])
        print("L", T[4])

if T[0] ==1 and T[1] == 1 and T[2] == 1 and T[3] == 1 and T[4] == 1: #условие для полного функционального набора
    print("Введен полный функциональный набор")
else:
    print("Набор не является полным функциональным")















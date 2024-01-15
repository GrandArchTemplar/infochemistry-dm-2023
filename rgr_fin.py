import math

# 1001 1110 1001 1010
def Line(a):                                                #проверяем  функцию на линейность
    for i in range(int(math.log2(len(a)))):                 #построение полинома Жегалкина
        b = ""
        t = 2 ** i
        k = t
        for j in range(1, int(len(a) / (t * 2)) + 1):
            q = ""
            for z in range(k - t, k):
                b += a[z]
                q += str(int(a[z]) ^ int(a[z + t]))
            b += q
            k += t * 2
        a = b
    for i in range(len(a)):                                  #проверяем на наличие коннъюнкций
        if a[i] == '0':
            continue
        k = bin(i)[2:].rjust(int(math.log2(len(a))), "0")
        sum_unit = sum(map(int, k))
        if sum_unit > 1:
            return 0
    return 1


def T0(a):                                                   #проверяем принадлежность к Т0
    if a[0] == '0':
        return 1
    else:
        return 0


def T1(a):                                                    #проверяем принадлежность к Т1
    if a[-1] == '1':
        return 1
    else:
        return 0


def Monot(a):                                                 #проверяем на монотонность
    for i in range(0, len(a), 2):
        if a[i] > a[i+1]:
            return 0
    return 1


def Samod(a):                                                  #проверяем на самодвойственность
    for i in range(len(a)//2):
        if a[i] == a[-i - 1]:
            return 0
    return 1

print('Введите количество функций')                             #запрашиваем количество функций
n = input()
f = 1 if n != '' else 0
for i in range(len(n)):
    if n[i].isdigit(): pass
    else:
        f = 0
        break
    if f == 1:
        n = int(n)
        if n > 0:
            pass
        else:
            f = 2

while f != 1:
    print('Число' + str('!!! ' if f == 0 else ' ') + 'больше нуля!!!')       #защита от дурака
    n = input()
    f = 1 if n != '' else 0
    for i in range(len(n)):
        if n[i].isdigit():
            pass
        else:
            f = 0
            break
    if f == 1:
        n = int(n)
        if n > 0:
            pass
        else:
            f = 2

n = int(n)
massive = []
sp2 = [2,4,8,16,32,64]

print('Введите вектора значений ваших функций')                             #ввод векторов значений функций
for i in range(n):
    while True:
        s = input()
        if s.count('0') + s.count('1') == len(s) and len(s) in sp2:
            massive.append(s)
            break
        elif s.count('0') + s.count('1') != len(s):                         #защита от дурака
            print('Должны быть только нули и единицы!')
        else:
            print('Длина вектора должна быть 2^n!')

flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
for i in range(n):
    print(T0(massive[i]), T1(massive[i]), Line(massive[i]), Monot(massive[i]), Samod(massive[i]))       #вывод
    if T0(massive[i]) == 0:
        flag1 = True
    if T1(massive[i]) == 0:
        flag2 = True
    if Line(massive[i]) == 0:
        flag3 = True
    if Monot(massive[i]) == 0:
        flag4 = True
    if Samod(massive[i]) == 0:
        flag5 = True
if flag1 and flag2 and flag3 and flag4 and flag5:
    print("Набор является полным")
else:
    print("Набор не является полным")



import math
import sys
A = []
B = []
C = []
D = []
f = 0
summ = 0
summ1 = 0
summ2 = 0
summT0 = 0
summT1 = 0
summM = 0
summL = 0
summSam = 0
T0 = []
T1 = []
M = []
Sam = []
L = []
count = 0
b = -1
d = 1


def fun():
    global f
    while f == 0:
        while True:
            try:
                n = int(input("Введите количество Функций: "))
                break
            except ValueError:
                print("Введите натуральное число")
        if n == 0 or n < 0:
            print("Введите натуральное число")
        else:
            f = 1
            print("Введите ваши функции в виде таблицы истинности")
            # генерация введенного числа полей ввода функций
            for i in range(0, n):
                x = input("Функция №" + str(1 + i) + ":")
                A.append(x)

    def fun1():
        global d
        for i in range(0, len(A)):
            C.append(list(A[i]))
            B.append(list(A[i]))
            # проверка на дурака
        for i in range(0, len(A)):
            a = math.log(len(B[i]), 2)
            # проверка на целочисленность
            if a.is_integer() == False or a == 0.0:
                print("Введены некорректные значения")
                d = 0
                break
            # проверка на нули и единицы
        for i in range(0, len(A)):
            for j in range(0, len(B[i])):
                if int(B[i][j]) != 0 and int(B[i][j]) != 1:
                    print("Введены некорректные значения")
                    d = 0
                    break
        if d == 0:
            sys.exit()
        # начинаем находить классы поста
        # класс самодвойственности
        for i in range(0, len(A)):
            for j in range(0, len(B[i]) // 2):
                global summ
                global Sam
                # здесь мы проверяем противоположные значения
                if (int(B[i][j]) + int(B[i][len(B[i]) - (j + 1)])) == 1:
                    summ += 1
            if summ == (len(B[i]) // 2):
                Sam.append(1)
                summ = 0
            else:
                Sam.append(0)
                summ = 0
        print('S', Sam, sep='  ')
        # класс T0
        for i in range(0, len(A)):
            if int(B[i][0]) == 0:
                T0.append(1)
            else:
                T0.append(0)
        print('T0', T0)
        # класс T1
        for i in range(0, len(A)):
            if int(B[i][len(B[i]) - 1]) == 0:
                T1.append(0)
            else:
                T1.append(1)
        print('T1', T1)
        # класс монотонности
        for i in range(0, len(A)):
            c = (''.join(B[i]))
            d = int(math.log(len(B[i]), 2))

            def Monoton(c, d):
                p = 2 ** d
                for k in range(0, p - 1):
                    for j in range(k + 1, p):
                        if (k & j) == k and int(B[i][k]) > int(B[i][j]):
                            return 0
                return 1

            M.append(Monoton(c, d))
        print('M', M, sep='  ')
        # класс линейности полинома
        # находим полином жегалкина
        for i in range(0, len(A)):
            global b
            for k in range(0, len(B[i])):
                b += 1
                for j in range(len(B[i]) - 1, b, -1):
                    B[i][j] = (int(B[i][j - 1]) + int(B[i][j])) % 2
        for i in range(0, len(A)):
            D = []
            global summ2
            if summ2 == 0:
                L.append(1)
                summ2 = 0
                summ1 = 0
            else:
                L.append(0)
                summ2 = 0
            # перевод в двоичную, чтобы соотнести полином Жегалкина с таблицей истинности, суммируем значения из таблицы, т.к. если сумма больше 1, то полином нелинейный
            for j in range(0, len(B[i])):
                if int(B[i][j]) == 1:
                    D.append(bin(j)[2:])
            for k in range(0, len(D)):
                D[k] = list(D[k])
            for j in range(0, len(D)):
                summ1 = 0
                summ2 = 0
                for k in range(0, len(D[j])):
                    summ1 += int(D[j][k])
                if summ1 > 1:
                    summ2 += 1
                    break
        print('L', L, sep='  ')
        for i in range(0, len(T0)):
            global summT0
            summT0 += T0[i]
        for i in range(0, len(T1)):
            global summT1
            summT1 += T1[i]
        for i in range(0, len(M)):
            global summM
            summM += M[i]
        for i in range(0, len(L)):
            global summL
            summL += L[i]
        for i in range(0, len(Sam)):
            global summSam
            summSam += Sam[i]

    return fun1()


fun()

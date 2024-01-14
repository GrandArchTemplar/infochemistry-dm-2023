def fuctor(n): #функция для факториала
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def coff(n, k):
    cof = fuctor(n) / (fuctor(k) * fuctor(n - k))
    return cof


def en(n, k):
    n = coff(n, k) * (kof1 ** (n - k)) * (kof2 ** (k))
    if n % 1 == 0:
        n = int(n)
    return n


e = input("Введите функцию: ")
n = int(input("Введите степень: "))
if n < 0: #защита от отрицательной степени
    print("Введите неотрицательную степень");
    exit();
i = 1
while e[i] != '+': #подсчет сколько символов до плюса в исходном выражении
    i += 1;

kof1 = e[1:(i - 1)] #первый коэффицент
if kof1 == '': #проверка на коэффицент1
    kof1 = 1
else:
    kof1 = float(kof1)

compl = False #логическая переменная, показывающая является ли число комплексным

if e[len(e) - 3] != 'i': #второй коэффициент, если не комплексное число
    kof2 = e[(i + 1):(len(e) - 2)]

elif e[len(e) - 3] == 'i': #второй коэффициент, если комплексное + смена логики на правду
    kof2 = e[(i + 1):(len(e) - 3)];
    compl = True;

if kof2 == '': #проверка на коэффицент1
    kof2 = 1
else:
    kof2 = float(kof2)
a = e[i - 1]  #название неизвестных
b = e[-2]


for i in range(n): #цикл повторяется столько раз, сколько изначальная степень
    if a != b and compl: #для комлексных
        if i % 4 == 0: #формат вывода - сначала функция отвечающая за коэффицент, потом подряд наши переменные(sep и end отвечают за перенос на следующую строку и отсутствие пробела после +)
            print(en(n, i), a * (n - i), b * i, '+', sep='', end='')
        elif i % 4 == 1:
            print(en(n, i), 'i', a * (n - i), b * i, '-', sep='', end='')
        elif i % 4 == 3:
            print(en(n, i), 'i', a * (n - i), b * i, '+', sep='', end='')
        elif i % 4 == 2:
            print(en(n, i), a * (n - i), b * i, '-', sep='', end='')
    if a != b and not compl:#для рациональных
        print(en(n, i), a * (n - i), b * i, '+', sep='', end='')
if a == b:#на случай совпадения названия переменных
    kof = kof1 + kof2
    if kof % 1 == 0:
        kof = int(kof)
    print((kof) ** n, a * n, sep='')

if a != b and compl: #финальный член бинома для комплексных
    if n % 2 == 0:
        print(en(n, n), b * n, sep='') #нет end т.к. дальше не нужно чтобы все шло в строчку
    else:
        print(en(n, n), 'i', b * n, sep='')

if a != b and not compl:#финальный член бинома для некомплексных
    print(en(n, n), b * n, sep='')
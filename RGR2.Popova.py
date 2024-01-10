def vvod_a():     #определение корректности вводимого числа,
    a = input()   #на случай если в качестве степени будет введено отрицательное число
    try:
        int(a)
        if int(a) > 1:
            return int(a)
        else:
            print("Введите натуральное/вещественное число", end='')
            print()
            return vvod_a()
    except ValueError:
        print("Введите натуральное/вещественное число", end='')
        print()
        return vvod_a()

def prepare(a):      #чтобы убрать точки в натуральных числах
    try:
        int(a)
        return int(a)
    except ValueError:
        return a

def f(n):   #считаем факториал
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * f(n-1)


def chis(k):    #с помощью Юникода определяем что перед нами: цифра или буква (для чисел)
    if (ord(k)>=48 and ord(k)<=57) or k == "." or k==',':
        return True
    return False


def bukv(i):    #с помощью Юникода определяем что перед нами: цифра или буква (для букав)
    if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123):
        return True
    else:
        return False


def vvod_chislo(a):   #определяем вводимое число
    b, c =[], []
    for i in a: b.append(i)
    for i in a: c.append(i)
    for i in range(len(b)):
        if b[i] == ' ': c.remove(' ')
    mas = [0,[],0,0,0,[],0,0]   #задаем массив вводимого числа для того, чтоб потом его раскладывать
    if c[0]=='-':   #определяет знак первого числа
        mas[0]='-'
        c.remove('-')
    d = list(map(lambda x: x, c))
    i=0
    while(chis(d[i])):  #первое число
        mas[1].append(d[i])
        i+=1
    if mas[1]==[]:
        mas[1]=1
    else:
        mas[1]=float(''.join(mas[1]))
    if bukv(d[i]):      #отвечает за то, чтоб первая буква множилась при возведении в степени и выводилась
        mas[2] = d[i]
        i+=1
    else:
        return 0
    if d[i] == '+':     #определяет знак второго числа
        mas[4] = "+"
    elif d[i] == '-':
        mas[4] = "-"
    else:
        return 0
    i+=1
    try: 
        while(chis(d[i])):      #второе число
            mas[5].append(d[i])
            i+=1
        if mas[5]==[]:
            mas[5]=1
        else:
            mas[5]=float(''.join(mas[5]))
        if bukv(d[i]):      #вторая буква #jndtxftn pf dsdjl dnjhjq ,erds
            if d[i]==mas[2]  or d[i] ==mas[3]:
                    return 0
            mas[6]= d[i]
            i+=1
        else:
            return 0
        try:
            if bukv(d[i]):
                if d[i]==d[i-1]:
                    return 0
                mas[7] = d[i]
                i+=1
            d[i+1]
            return 0
        except IndexError:
            return mas
    except IndexError:
        return 0
    return 0

def correct_chislo(a):
    if vvod_chislo(a) == 0:
        print("Введите натуральное/вещественное число")
        a = correct_chislo(str(input()))
        return correct_chislo(a)
    return a

def func(n,x,y,a,b):
    for j in range(n+1):
        c = f(n)/(f(n-j)*f(j))                  #используется формула Cn по k из бинома Ньютона,
        k = prepare(c*(x**(n-j))*(y**j))        #чтобы определить коэффициент, который дает степень
        if k != 0:
            if k > 0:
                if j!=0:
                    print("+",end='')
            elif k < 0:
                print("-",end='')
            if abs(k) != 1:
                print(abs(k), end='')
            print(a*(n-j), end='')
            print(b*j, end='')

print("Введите выражение: ")
ch = correct_chislo(str(input()))
print("Введите степень: ")
n = vvod_a()
mas = vvod_chislo(ch)
x = mas[1]
if mas[0] != 0:
    x = 0-x
y=mas[5]
if mas[4] == '-':
    y = 0-y
i=[0,0]
a = mas[2]
b = mas[6]

print("Результат: ")
if i[0] ==0 and i[1] == 0:
    func(n,x,y,a,b)
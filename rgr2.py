vvod1 = input("Введите выражение вида (ax+by): ")
n = int(input("Введите степень n: "))
if vvod1.startswith('-') and (n%2)!=0:
    print('-', end="")
char = ""
letters=[]
for x in vvod1:
    char = ""
    if x.isalpha(): #работаем с буквами
        char = "".join([char, x])
        letters.append(str(char))
def fact(m): #факториал
    f = 1
    for i in range(1, m + 1):
        f = f * i
    return f
def koef(n, k): # бином ньютона
    x = fact(n)
    y = fact(k)
    c = fact(n - k)
    return x // (y * c)
def convert_to_int_or_float(n, k, a, b):
    num = koef(n, k) * (a ** (n - k)) * (b ** k)
    if num.is_integer():
        return int(num)
    else:
        return num
def pow(n, k, letters): #возведение букв в степень
    letter1 = str(letters[0]) * (n - k)
    letter2 = str(letters[1]) * k
    return letter1 + letter2
def ahtung(n, letters, integers): #ахтунг: буквы равны
    letter = str(letters[0]) * n
    integer = (float(integers[0])+float(integers[1])) ** n
    return str(integer)+letter
length = len(vvod1)
integers = []
num = ''
for char in vvod1: #работаем с цифрами
    if char.isdigit() or char == ".":
        num += char
    elif num:
        integers.append(float(num))
        num = ''
if num:
    integers.append(float(num))
k = 0
if str(letters[0])!=str(letters[1]):
    for i in range(0, len(integers)):
        a = float(integers[0])
        b = float(integers[1])
        while k <= n:
            print(convert_to_int_or_float(n, k, a, b), pow(n, k, letters), sep='', end='')
            k = k + 1
            if k <= n:
                if vvod1.count('-')==2 and (n%2)!=0:
                    print(" - ", end='')
                elif vvod1.count('-')==2 and (n%2)==0:
                    print(" + ", end='')
                elif vvod1.startswith('-') and (n%2)!=0:
                    operation = '-+'[k % 2]  # + on even, - on odd
                    print(' ' + operation + '', end=' ')
                elif vvod1.startswith('-') and (n%2)==0:
                    operation = '+-'[k % 2]  # + on even, - on odd
                    print(' ' + operation + '', end=' ')
                elif '-' in vvod1:
                    operation = '+-'[k % 2]  # + on even, - on odd
                    print(' ' + operation + '', end=' ')
                else:
                    print(" + ", end='')
else:
    print(ahtung(n, letters, integers))


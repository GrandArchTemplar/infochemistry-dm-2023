# Завалинова Мария 1 курс инфохимии
def fuctorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def coefficient(n, k):
    coef = fuctorial(n) / (fuctorial(k) * fuctorial(n - k))
    return coef

def finalcoefficient(n, k):
    n = coefficient(n, k) * (coef1** (n - k)) * (coof2 ** (k))
    if n % 1 == 0:
        n = int(n)
    return n

def step_input(promt):
    step = input(promt)
    try:
        int(step)
        if int(step)>0:
            return int(step)
        else:
            return step_input('Пожалуйста, введите положительное значение степени')
    except ValueError:
        print('Пожалуйста, введите положительную степень!! Попробуйте еще раз', end='')
        return step_input()




form = input("Введите выражение вида (ax+by): ")
step = step_input("Введите степень: ")

i = 1
while form[i] != '+':
    i += 1;
coef1 = form[1:(i - 1)]
if coef1 == '':
    coef1= 1
else:
    coef1 = (float(coef1))

complex = False

if form[len(form) - 3] != 'i':
    coof2 = form[(i + 1):(len(form) - 2)]

elif form[len(form) - 3] == 'i':
    coof2 = form[(i + 1):(len(form) - 3)];
    complex = True;

if coof2 == '':
    coof2= 1
else:
    coof2 = float(coof2)
a = form[i - 1]
b = form[-2]



for i in range(step):
    if a != b and complex:
        if i % 4 == 0:
            print(finalcoefficient(step, i), a * (step - i), b * i, '+', sep='', end='')
        elif i % 4 == 1:
            print(finalcoefficient(step, i), 'i', a * (step - i), b * i, '-', sep='', end='')
        elif i % 4 == 3:
            print(finalcoefficient(step, i), 'i', a * (step - i), b * i, '+', sep='', end='')
        elif i % 4 == 2:
            print(finalcoefficient(step, i), a * (step- i), b * i, '-', sep='', end='')
    if a != b and not complex:
        print(finalcoefficient(step, i), a * (step - i), b * i, '+', sep='', end='')
if a == b:
    coef = coef1 + coof2
    if coef % 1 == 0:
        kof = int(coef)
    print((coef) ** step, a * step, sep='')

if a != b and complex:
    if step % 2 == 0:
        print(finalcoefficient(step, step), b * step, sep='')
    else:
        print(finalcoefficient(step, step), 'i', b * step, sep='')

if a != b and not complex:
    print(finalcoefficient(step, step), b * step, sep='')








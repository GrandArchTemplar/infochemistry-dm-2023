'''
Ввод
осуществляется с помощью стандартного ввода с клавиатуры, переменная a имеет тип данных string, а st-int
a хранит в себе изначальное выражение, которое проверяется на наличие скобок в начале и в конце 
st хранит в себе степень, которая проверяется на условие >= 0
защита от дурака будет вызываться пока не будет введено верное выражение или степень
'''



a = ''
st = -2
print("Введите выражение:")
while ("(" not in a) or (")" not in a):
    a = input()
    if ("(" not in a) or (")" not in a):
        print("Введите выражение в корректной форме.")    
print("Введите степень:")
while st < 0:
    st = int(input())
    if st < 0:
        print("Введите неотрицательную степень.")




# stepen понадобится нам при наличии комплексного числа


stepen = 0



'''
znaki позволит нам сделать split, то есть разбить строку на 2 переменных
znaki будет хранить в себе все знаки + и -, хранящиеся в переменной a
максимальное количество знаков, которые будут храниться в znaki - 2, из-за специфики задания
(-0.5a + 4ib)
 при данном примере znaki= -+
'''


znaki=''
for i in a:
    if i=="+" or i=="-":
        znaki += i



'''
Разделяем уравнение на части, используя znaki
получаем массив terms
Может возникнуть такой случай, что у нас будут 2 - в znaki
тогда строка разобьётся на 3 элемента
чтобы это предотвратить делаем проверку на количество элементов в znaki
если их больше 1 то, срезаем первый и строка делится ровно на 2 элемента 
'''


terms = a.replace(' ', '').replace('(', '').replace(')', '').split(znaki[len(znaki)-1])
if len(znaki) > 1:
    if znaki[0] == znaki [1]:
        terms = terms[1:3]
cicl = []
bukv = []



'''
Создаём 2 переменных coefficient и variable
Проходимся по каждому символу в каждом из элементов массива terms
Проверяем на isalpha (буква) и isdigit (цифра) и кладём значения в соответствующие переменные cicl и bukv
'''


for term in terms:
    coefficient, variable = "", ""
    for char in term:
        if char.isalpha():
            variable += char
        elif char.isdigit() or char in ['.', '-']:
            coefficient += char
    bukv.append(variable)
    cicl.append(coefficient)


'''
firstcof 1 коэффициент для вычислений
secondcof соответственно второй
'''


firstcof = 0
secondcof = 0


# Добавляем значения в коэффициенты с проверкой на единичный, например a+b


for term in terms:
    if bukv[0] in term:
        if term.replace(bukv[0], '') == '':
            firstcof += 1
        else:
            firstcof += float(term.replace(bukv[0], ''))
    elif bukv[1] in term:
        if term.replace(bukv[1], '') == '':
            secondcof += 1
        else:
            secondcof += float(term.replace(bukv[1], ''))
            

# Смена знаков коэффициентов, т.к. при использовании znaki они теряются

    
if len(znaki)>1:
    if znaki[0]=='-' and firstcof>0:
        firstcof=firstcof*(-1)
    if znaki[1]=='-' and secondcof>0:
        secondcof=secondcof*(-1)
else:
    if znaki[0]=='-' and secondcof>0:
        secondcof=secondcof*(-1)




# Собственно наш будущий вывод

        
result = ""



'''
Данная функция вычисляет биномиальный коэффициент
Функция работает следующим образом:
Если k=0 или k=n, то биномиальный коэффициент равен 1. Это является частным случаем формулы для биномиального коэффициента.
Если 0<k<n, то биномиальный коэффициент можно вычислить по формуле.
Она является рекуррентной формулой для биномиальных коэффициентов.
'''



def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)


result = ""




'''
Частный случай, если у нас задана всего 1 переменная, например (3x+5x)
Также встроена поддержка комплексных чисел
Stepen будет считать количество i в выводе
При i кратном 2 они будут убираться. т.к. i*i=-1
При i не кратном 2 уберутся все, кроме 1, которая поставится в начало
В зависимости от количества i будет меняться знак
При  i=1 знак +     i=2 знак -    i=3 знак -    i=4 знак +    i=5 знак +
Можно выявить закономерность и поставить условия i=1; i кратно 4; и остаток от деления на 4 равен 1 для знака +
'''




if secondcof==0:
    term_coefficient = firstcof**(st)
    term_variables = bukv[0] * (st)
    stepen=term_variables.count('i')
    if stepen % 2 != 0:
        term_variables=term_variables.replace('i', '')
        term_variables='i'+term_variables
    if stepen % 2 == 0:
        term_variables=term_variables.replace('i', '')
    term = f"{term_coefficient}{term_variables}"
    if stepen == 1 or stepen % 4 == 1 or stepen %4 == 0 :
            result = ""
    else:
            result += "-"
    result += term
    



else:
    for i in range(st + 1):
        term_coefficient = binomial_coefficient(st, i) * firstcof**(st - i) * secondcof**i
        term_variables = bukv[0] * (st - i) + bukv[1] * i 
        stepen=term_variables.count('i')
        if stepen % 2 != 0:
            term_variables=term_variables.replace('i', '')
            term_variables='i'+term_variables
        if stepen % 2 == 0:
            term_variables=term_variables.replace('i', '')
        term = f"{term_coefficient}{term_variables}"
        if i != 0 and (stepen == 1 or stepen % 4 == 1 or stepen %4 == 0):
            if term_coefficient>=0:
                result += " + "
            else:
                result += " - "
                term_coefficient=term_coefficient*(-1)
        elif i != 0:
            if term_coefficient>=0:
                result += " - "
            else:
                result += " + "
                term_coefficient=term_coefficient*(-1)
        term = f"{term_coefficient}{term_variables}"
        result += term

'''
Пояснение к блоку выше
Здесь общий случай с 2 разными переменными
Алгоритм для комплексных чисел тот же
С помощью биномиального коэффициента мы можем посчитать нужные нам значения коэффициентов
Чтобы определить знак после числа и не поставить лишний, мы смотрим на количество i, а затем на знак коэффициентов, чтобы избежать ситуаций типа 100xxx--50xxy
Если коэффициент отрицательный и i подходит на +, мы его умножаем на минус 1 и ставим знак минус, чтобы пробелы смотрелись красиво :)
И в обратную сторону также, если если коэффициент отрицательный и i подходит на -, мы его умножаем на минус 1 и ставим знак плюс
И наконец объединяем переменные и коэффициенты
Добавляем в result
'''

'''
Вывод ответа
'''
        
print(result)


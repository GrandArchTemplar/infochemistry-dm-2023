import math

#Список букв для разделения входной строки на коэффициент и операнд
WHITELIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'j', '(', ')', '+', '-']

#Класс MyComplex наследующий класс complex для форматированного вывода комплексных чисел
class MyComplex(complex): 
    #Перегрузка функции преобразования в строчку
    def __str__(self):
        result = ''
        if self.real != 0 and self.imag != 0:
            if abs(self.imag) == 1:
                result = f' + ({int(self.real) if self.real.is_integer() else self.real}{"+" if self.imag > 0 else ""}i)'
            else:
                result = f' + ({int(self.real) if self.real.is_integer() else self.real}{"+" if self.imag > 0 else ""}{int(self.imag) if self.imag.is_integer() else self.imag}i)'
        else:
            if self.real != 0:
                if self.real.is_integer():
                    result += f'{" + " if self.real > 0 else ""}{" - " if self.real < 0 else ""}{abs(int(self.real))}'
                else:
                    result += f'{" + " if self.real > 0 else ""}{" - " if self.real < 0 else ""}{abs(self.real)}'
            if self.imag != 0:
                if abs(self.imag) == 1:
                    result += f'{" + " if self.imag > 0 else ""}{" - " if self.imag < 0 else ""}i'
                else:
                    if self.imag.is_integer():
                        result += f'{" + " if self.imag > 0 else ""}{" - " if self.imag < 0 else ""}{abs(int(self.imag))}i'
                    else:
                        result += f'{" + " if self.imag > 0 else ""}{" - " if self.imag < 0 else ""}{abs(self.imag)}i'
        return result

def transform(s:str, n:int):
    i = 0
    s = s[s.find('(')+1:]
    s = s[:s.rfind(')')]
    f1, f2 = s.replace('i','j').split(' + ')
    for symbol in f1:
        if symbol not in WHITELIST:
            i = f1.index(symbol)
            break
    k1 = complex(f1[:i])
    l1 = f1[i:]

    for symbol in f2:
        if symbol not in WHITELIST:
            i = f2.index(symbol)
            break
    k2 = complex(f2[:i])
    l2 = f2[i:]

    expansion = binomial_expansion(k1,k2,n)
    result = ''
    for i in range(n+1):
        if expansion[i] == 0:
            result += ''
        else:
            result += f'{expansion[i]}{l1*(n-i)}{l2*i}'

    if result[1] == '-':
        return '-'+result[3:]
    return result[3:]

def binomial_coefficient(n:int, k:int):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def binomial_expansion(a, b, n:int):
    expansion = []
    for k in range(n + 1):
        coefficient = binomial_coefficient(n, k)
        term = coefficient * (a ** (n - k)) * (b ** k)
        expansion.append(term)
    
    #Преобразование комплексных чисел в объекты класса MyComplex для форматированного вывода
    expansion = [MyComplex(i) for i in expansion]
    return expansion

if __name__ == '__main__':
    print('Пример ввода выражений (вводите пробелы как в примере)')
    print('Выражение без комплексных чисел: (ax + by)')    
    print('Выражение с одним комплексным числом: ((a±ci)x + by) или (ax + (b±di)y)')
    print('Выражение с двумя комплексными числами: ((a±ci)x + (b±di)y)')
    print('Недопустимые буквы для операндов i и j')
    s = input("Введите выражение: ")
    n = int(input("Введите степень: "))
    print(transform(s,n))
    
    #Тест
    # print(transform('(0.5a + 4ib)',3))

# комплексные числа представлены списком из двух вещественных чисел
# первое - действительная, вторая - мнимая часть числа 

# получение буквы и коэффициента из выражения вида 5a, 5ia, (2+5i)a
def get_coef(expression):
    # убираем лишние пробелы
    expression = expression.strip()
    # проверяем выражение на пустоту и находим и убираем переменную (в конце)
    if expression == '' or not expression[-1].isalpha():
        return False, []
    variable = expression[-1]
    expression = expression[:-1:].strip()
    # если больше ничего нет, значит коэффициент - единица
    if expression == '':
        return True, [variable, [1.0, 0.0]]
    # находим коэффициент - действительный, мнимый или комплексный
    a, b = '0', '0' # действительная и мнимая части
    b_sign = 1 # знак мнимой части (в случае -i будет -1)
    # если есть скобки, коэффициент комплексный
    if expression[0] == '(':
        # проверяем наличие закрывающей скобки
        if expression[-1] != ')':
            return False, []
        expression = expression[1:-1:].strip()
        # разделяем по плюсу или минусу
        if expression.find('+') != -1:
            expression = expression.split('+')
        elif expression.find('-') != -1:
            expression = expression.split('-')
            b_sign = -1
        else:
            return False, []
        # находим действительную и мнимую (с i) части
        a, b = expression[0].strip(), expression[1].strip()
        if a.find('i') != -1:
            a, b = b, a
        if a.find('i') != -1 or b[-1] != 'i' or len(expression) > 2:
            return False, []
        b = b[:-1:] # из мнимой части убираем i
    # случай чисто мнимого числа
    elif expression[-1] == 'i':
        b = expression[:-1:].strip()
        if b == '':
            b = '1.0'
    # случай действительного числа
    else:
        a = expression
    # преобразуем выделенные числа в вещественный формат
    try:
        return True, [variable, [float(a), float(b) * b_sign]]
    except ValueError:
        return False, []
    
# разбор всего выражения: получения двух букв и двух (комплексных) коэффициентов
def parse(expression):
    # проверка на пустоту
    if expression == '':
        return False, 'Пустое выражение'
    # первый и последний символы (по условию ввода) - скобки
    if expression[0] != '(' or expression[-1] != ')':
        return False, 'Ошибка: выражение не в скобках'
    # убираем скобки
    expression = expression[1:-1:]
    # находим в выражении плюс и скобку (возможна при комплексном коэффициенте)
    plus = expression.find('+')
    brace = expression.find(')')
    # если плюса нет, ввод некорректен
    if plus == -1:
        return False, 'Ошибка: в выражении нет знака "+"'
    # если скобка раньше плюса, просто делим выражение по плюсу
    if brace < plus:
        expression = expression.split('+', 1)
    # если плюс раньше скобки, нужно разделить выражение по следующему плюсу
    else:
        plus = expression.find('+', plus + 1)
        if plus == -1:
            return False, 'Ошибка: в выражении нет знака "+"'
        expression = [expression[:plus:], expression[plus + 1::]]
    # получаем коэффициенты и проверяем их
    a, b = get_coef(expression[0]), get_coef(expression[1])
    if a[0] == False or b[0] == False:
        return False, 'Ошибка ввода коэффициентов'
    return True, a[1], b[1]

# функция умножения комплексных чисел
def complex_mult(x, y):
    a, b = x[0], x[1]
    c, d = y[0], y[1]
    return [a * c - b * d, b * c + a * d]

# функция возведения комплексного числа в степень (через умножение)
def complex_power(number, power):
    res = [1.0, 0.0]
    for _ in range(power):
        res = complex_mult(res, number)
    return res

# функия вычисления факториала    
def factorial(number):
    if number < 2:
        return 1
    return number * factorial(number - 1)

# функция вычисления биномиального коэффициента
def binomial_coef(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# преобразование комплексного числа к строке
def str_complex(number, k):
    a, b = number[0], number[1] # вещественная и мнимая части числа
    # общий знак числа (соответствует вещественной части)
    # в случае первого числа в выражении выводим только минус
    if k == 0:
        sign = '' if a >= 0 else '-'
    # в случае середины выводим плюс или минус (с пробелами для красоты)
    else:
        sign = ' + ' if a >= 0 else ' - '
    # если общий знак минус - меняем знаки вещественной и мнимой частей для вывода
    # (чтобы не выводить минус дважды)
    if a < 0:
        a, b = -a, -b
    # если ненулевые и вещественная, и мнимая части, выводим полное число в скобках
    if a != 0 and b != 0:
        if b == 1 or b == -1:
            return '{0:s}({1:g}{2:s}i)'.format(sign, a, '-' if b < 0 else '+')
        return '{0:s}({1:g}{2:s}{3:g}i)'.format(sign, a, '' if b < 0 else '+', b)
    # иначе выводим только вещественную/мнимую часть
    else:
        i = 'i' if a == 0 else ''
        n = a if b == 0 else b
        if b < 0:
            sign = ' - ' if k > 0 else '-'
            n = -n
        return sign + ('{0:g}{1:s}'.format(n, i) if n != 1 else i)

# основная программа
def main():
    # ввод и проверка выражения
    expr = parse(input('Введите выражение: '))
    while not expr[0]:
        print(expr[1])
        expr = parse(input('Введите выражение: '))
    n = int(input('Введите степень: '))
    # вычисление степени по формуле бинома Ньютона
    for k in range(n + 1):
        # биномиальный коэффициент
        b = binomial_coef(n, k)
        # степени коэффициентов, умноженные на биномиальный коэффициент
        coef = complex_mult([b, 0.0], complex_mult(complex_power(expr[1][1], n - k), complex_power(expr[2][1], k)))
        # вывод коэффициента
        print(str_complex(coef, k), end='')
        # вывод степени переменной
        for i in range(n - k):
            print(expr[1][0], end='')
        for i in range(k):
            print(expr[2][0], end='')
            
if __name__ == '__main__':
    main()
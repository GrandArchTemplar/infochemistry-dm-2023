# Функция для вычисления биномиальных коэффициентов
def binom(n, k):
    # n! / (k! * (n-k)!)
    result = 1
    for i in range(1, k+1):
        result = result * (n - i + 1) // i
    return result

# Функция для раскрытия выражения вида (ax+by)^n
def expand(ax, by, n):
    # Инициализируем пустой список для хранения слагаемых
    terms = []
    # Перебираем все возможные степени x и y
    for i in range(n+1):
        # Вычисляем биномиальный коэффициент
        coeff = binom(n, i)
        # Вычисляем коэффициенты a и b
        a_coeff = ax ** (n - i)
        b_coeff = by ** i
        # Составляем слагаемое в виде строки
        term = str(coeff * a_coeff * b_coeff)
        # Добавляем степени x и y, если они не равны нулю
        if n - i > 0:
            term += "x"
            if n - i > 1:
                term += "^" + str(n - i)
        if i > 0:
            term += "y"
            if i > 1:
                term += "^" + str(i)
        # Добавляем слагаемое в список
        terms.append(term)
    # Соединяем слагаемые в одну строку с плюсами
    expansion = " + ".join(terms)
    # Возвращаем результат
    return expansion

# Пример ввода и вывода
expression = input("Введите выражение вида (ax+by) (где a,b - целые или вещественные числа; калькулятор не считает комплексные числа:(( ): ")
power = int(input("Введите степень n: "))
# Извлекаем коэффициенты a и b из выражения
ax, by = expression.strip("()").split("+")
# Вызываем функцию раскрытия
result = expand(float(ax.split("x")[0]), float(by.split("y")[0]), power)
# Выводим результат
print("Результат выражения:", result)
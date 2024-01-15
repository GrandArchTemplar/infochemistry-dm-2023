# Функция для вычисления биномиальных коэффициентов
def binom(n, k):
    # n! / (k! * (n-k)!)
    result = 1
    for i in range(1, k+1):
        result = result * (n - i + 1) // i
    return result

# Функция для раскрытия выражения вида (ax+by)^n
def asd(ax, by, j):

    cifri = []
    # Перебираем все возможные степени x и y
    for i in range(j+1):
        # Вычисляем биномиальный коэффициент
        coeff = binom(j, i)
        # Вычисляем коэффициенты a и b
        a_coeff = ax ** (j - i)
        b_coeff = by ** i
        # Составляем слагаемое в виде строки
        term = str(coeff * a_coeff * b_coeff)
        # Добавляем степени x и y, если они не равны нулю
        if j - i > 0:
            term += o
            if j - i > 1:
                term += "^" + str(j - i)
        if i > 0:
            term += p
            if i > 1:
                term += "^" + str(i)
        cifri.append(term)
    expansion = " + ".join(cifri)
    return expansion

# Пример ввода и вывода
o = str(input("Введите 1ю переменную "))
p = str(input("Введите вторую переменную "))
virajenie = input("Введите выражение вида (ax+by) (где a,b - целые или вещественные числа;x,y - введенные вами переменные): ")
power = int(input("Введите степень n: "))
# Извлекаем коэффициенты a и b из выражения
ax, by = virajenie.strip("()").split("+")
# Вызываем функцию раскрытия
itog = asd(float(ax.split(o)[0]), float(by.split(p)[0]), power)
# Выводим результат
print("Результат выражения:", itog)
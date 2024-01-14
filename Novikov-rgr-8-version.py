import math

# Функция для ввода количества функций и их обработки.
def main():
    n = int(input("Введите количество функций: "))  # Ввод количества функций.

    if n <= 0:
        print("Введите n > 0!")
        return

    function_values = []
    for i in range(n):
        function = input(f"Введите функцию {i + 1}: ")  # Ввод функции.
        if not is_binary_function(function):
            print("Введены некорректные значения функций. Функция должна состоять только из 0 и 1.")
            return
        function_values.append(function)

    analyze_functions(function_values)

# Проверяет, состоит ли функция только из 0 и 1.
def is_binary_function(function):
    return all(c in ['0', '1'] for c in function)

# Анализирует функции на принадлежность к классам Поста.
def analyze_functions(functions):
    Sam, T0, T1, M, L = [], [], [], [], []  # Списки для классов Поста.

    for function in functions:  # Для каждой функции
        # Проверяем принадлежность к каждому классу Поста и добавляем результат в соответствующий список.
        Sam.append(check_self_duality(function))
        T0.append(check_zero_preserving(function))
        T1.append(check_one_preserving(function))
        M.append(check_monotonicity(function))
        L.append(check_linearity(function))

    # Проверяем, является ли набор функций полным.
    is_full_set = all(check_completeness(cl) for cl in [Sam, T0, T1, M, L])
    print(f"Набор {'полный' if is_full_set else 'неполный'}")  # Выводим сообщение о полноте набора.

    for i, function in enumerate(functions):  # Выводим информацию о классах Поста для каждой функции.
        class_msg = f'Функция {i + 1}: Sam={Sam[i]}, T0={T0[i]}, T1={T1[i]}, Monotone={M[i]}, Линейность={L[i]}'
        print(class_msg)

# Проверяет, является ли функция самодвойственной.
def check_self_duality(function):
    half_len = len(function) // 2  # Размер половины функции.
    return all(int(function[i]) + int(function[-(i + 1)]) == 1 for i in range(half_len))

# Проверяет, сохраняет ли функция ноль.
def check_zero_preserving(function):
    return int(function[0]) == 0

# Проверяет, сохраняет ли функция единицу.
def check_one_preserving(function):
    return int(function[-1]) == 1

# Проверяет, является ли функция монотонной.
def check_monotonicity(function):
    d = int(math.log2(len(function)))  # Количество переменных функции.
    for i in range(len(function) - 1):
        for j in range(i + 1, len(function)):
            if (i & j) == i and int(function[i]) > int(function[j]):
                return False  # Если функция не монотонна, возвращаем False.
    return True  # Если функция монотонна, возвращаем True.

# Проверяет, является ли функция линейной.
def check_linearity(function):
    for i in range(len(function)):
        if int(function[i]) == 1:
            if sum(map(int, bin(i)[2:])) > 1:  # Считаем количество единиц в двоичном представлении индекса.
                return False  # Если единиц больше одной, функция не линейна.
    return True  # Если функция линейна, возвращаем True.
if __name__ == "__main__":
    main()
# Проверяет, является ли набор функций полным.
def check_completeness(class_list):
    return all(x == 1 for x in class_list)  # Возвращает True, если все элементы списка равны 1.



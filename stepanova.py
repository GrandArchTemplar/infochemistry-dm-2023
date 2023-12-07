from itertools import product
from typing import List, Tuple

def check_T0(table: List[int]) -> bool:
    """ Проверка на принадлежность к классу Т_0 (сохраняющий 0). """
    return table[0] == 0

def check_T1(table: List[int], n_vars: int) -> bool:
    """ Проверка на принадлежность к классу Т_1 (сохраняющий 1). """
    return table[-1] == 1

def check_M(table: List[int], n_vars: int) -> bool:
    """ Проверка на принадлежность к классу М (монотонность). """
    for i in range(len(table) - 1):
        for j in range(i + 1, len(table)):
            binary_i = format(i, f'0{n_vars}b')
            binary_j = format(j, f'0{n_vars}b')
            if all(bit_i <= bit_j for bit_i, bit_j in zip(binary_i, binary_j)):
                if table[i] > table[j]:
                    return False
    return True

def check_S(table: List[int], n_vars: int) -> bool:
    """ Проверка на принадлежность к классу S (самодвойственность). """
    for i in range(len(table) // 2):
        if table[i] == table[-1 - i]:
            return False
    return True

def check_L(table: List[int], n_vars: int) -> bool:
    """ Проверка на принадлежность к классу L (линейность). """
    for combination in product([0, 1], repeat=n_vars):
        sum_comb = sum(combination) % 2
        index = int("".join(map(str, combination)), 2)
        if table[index] != sum_comb:
            return False
    return True

def read_function():
    """ Считывает булеву функцию от пользователя. """
    while True:
        try:
            n = int(input("Введите количество переменных для функции: "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Пожалуйста, введите положительное целое число.")

    while True:
        try:
            f = list(map(int, input(f"Введите таблицу истинности (как последовательность из 0 и 1, длиной {2 ** n}): ").split()))
            if len(f) != 2 ** n or any(v not in [0, 1] for v in f):
                raise ValueError
            break
        except ValueError:
            print(f"Пожалуйста, введите последовательность из {2 ** n} нулей и единиц.")

    return f, n
def main():
    functions = []
    # Изменяем структуру для хранения принадлежности каждой функции к каждому классу
    post_classes = {"T0": [], "T1": [], "M": [], "S": [], "L": []}

    while True:
        f, n = read_function()
        functions.append((f, n))

        # Check and assign Post classes
        post_classes["T0"].append(1 if check_T0(f) else 0)
        post_classes["T1"].append(1 if check_T1(f, n) else 0)
        post_classes["M"].append(1 if check_M(f, n) else 0)
        post_classes["S"].append(1 if check_S(f, n) else 0)
        post_classes["L"].append(1 if check_L(f, n) else 0)

        if input("Желаете добавить еще функцию? (да/нет): ").lower() != "да":          break

    # Check for completeness
    is_complete = all([any(post_classes[cls]) for cls in post_classes])

    # Вывод результатов
    print("\nПринадлежность к классам Поста:")
    for cls in post_classes:
        print(f"{cls}: {post_classes[cls]}")

    print(f"\nЯвляется ли набор функций полным? {'Да' if is_complete else 'Нет'}")

main()
import sympy as sp
import re

def expand_expression(expr, power):
    # Создаем символы для всех латинских букв
    symbols = [sp.symbols(letter) for letter in 'abcdefghijklmnopqrstuvwxyz']

    # Создаем словарь для замены символов в выражении
    replace_dict = {f"{letter}": symbol for letter, symbol in zip('abcdefghijklmnopqrstuvwxyz', symbols)}

    # Заменяем буквы в выражении на соответствующие символы
    expr = sp.sympify(str(expr))
    expr = expr.subs(replace_dict)

    # Раскрываем выражение в степени
    expanded_expr = sp.expand(expr ** power)

    return expanded_expr

def transform_expression(input_str):
    # Паттерн для поиска выражений вида 'x**n' и 'y**n', где n - целое число
    pattern = re.compile(r'([a-z])\*\*(\d+)')

    def replace_match(match):
        variable, power = match.groups()
        return variable * int(power)

    transformed_str = pattern.sub(replace_match, input_str)
    return transformed_str

def main():
    # Ввод пользователем выражения и степени
    input_expr = input("Введите выражение вида ax+by (например 2x+8y , 4e + y + l - 9f): ")
    while True:
        input_power = input("Введите положительную степень n (например 2): ")
        try:
            power = int(input_power)
            if power > 0:
                break  # Прерываем цикл, если степень положительная
            else:
                print("Ошибка: Введите положительное значение для степени.")
        except ValueError:
            print("Ошибка: Введите корректное целое число для степени.")

    try:
        # Преобразование входных данных в SymPy-выражения
        # Добавление '*' перед каждым символом (a-z), если перед символом есть число
        expr = sp.sympify(re.sub(r'(\d)([a-z])', r'\1*\2', input_expr))

        # Расширение выражения и трансформация результата
        result_expr = expand_expression(expr, power)
        result = transform_expression(str(result_expr))
        result_str = str(result).replace('*', '')

        print(result_str)

    except (sp.SympifyError, ValueError):
        print("Ошибка ввода. Пожалуйста, введите корректное выражение и степень.")

if __name__ == "__main__":
    main()

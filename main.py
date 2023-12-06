def is_tautology(function):
    """ Проверка на тождественную истину """
    return all(function)

def is_self_dual(function):
    """ Проверка на самодвойственность """
    n = len(function)
    return all(function[i] != function[n - i - 1] for i in range(n // 2))

def is_monotone(function):
    """ Проверка на монотонность """
    for i in range(len(function)):
        for j in range(len(function)):
            if i | j == j and function[i] > function[j]:
                return False
    return True

def is_linear(function):
    """ Проверка на линейность """
    for i in range(len(function)):
        for j in range(len(function)):
            if function[i & j] != function[i] & function[j]:
                return False
    return True

def is_preserving_zero(function):
    """ Проверка на сохранение нуля """
    return function[0] == 0

def is_preserving_one(function):
    """ Проверка на сохранение единицы """
    return function[-1] == 1

def classify_function(function):
    """ Классификация функции по классам Поста """
    result = {
        'Тождественная истина': is_tautology(function),
        'Самодвойственность': is_self_dual(function),
        'Монотонность': is_monotone(function),
        'Линейность': is_linear(function),
        'Сохранение нуля': is_preserving_zero(function),
        'Сохранение единицы': is_preserving_one(function)
    }
    return result

def is_complete_set(functions):
    """ Проверка на полноту системы функций """
    properties = ['Тождественная истина', 'Самодвойственность', 'Монотонность', 'Линейность', 'Сохранение нуля', 'Сохранение единицы']
    for property in properties:
        if all(not classify_function(function)[property] for function in functions):
            return False
    return True

def input_functions():
    """ Ввод функций пользователем """
    functions = []
    while True:
        try:
            function = input("Введите функцию или 'q' для выхода: ")
            if function == 'q':
                break
            if not all(c in '01' for c in function):
                raise ValueError("Функция должна состоять только из 0 и 1, вы не прошли проверку на дурака :()")
            functions.append([int(c) for c in function])
        except ValueError:
            print(f"Ошибка :(")
    return functions

def main():
    """ Основная функция программы """
    print("Программа для определения классов Поста и проверки на полноту системы логических функций.")
    functions = input_functions()
    
    for i, function in enumerate(functions):
        print(f"\nФункция {i+1}: {function}")
        for property, value in classify_function(function).items():
            print(f"{property}: {'Да' if value else 'Нет'}")

    print(f"\nСистема функций {'полна' if is_complete_set(functions) else 'не полна'}.")

if __name__ == "__main__":
    main()

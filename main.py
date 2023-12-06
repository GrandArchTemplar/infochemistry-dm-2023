#Код написан студентом 1 курса Инфохимии Завалиновой Марией
def number_input(promt):
    x = input(promt)
    try:
        int(x)
        if int(x) > 0:
            return int(x)
        else:
            return number_input('Пожалуйста, введите натуральное число! Попробуйте еще раз')
    except ValueError:
        print('Пожалуйста, введите натуральное число!! Попробуйте еще раз', end='')
        return number_input()


def args_input():
    x = input()
    try:
        int(x)
        if int(x) == 0 or int(x) == 1:
            return int(x)
        else:
            print('Вы ввели не 0 или 1! Попробуйте еще раз', end='')
            return args_input()
    except ValueError:
        print('Вы ввели не 0 или 1! Попробуйте еще раз', end='')
        return args_input()


def get_boolean_values():
    boolean_values = []
    boolean_functions = []

    num_func = number_input("Введите количество булевых функций: ")

    for func_n in range(1, num_func + 1):
        n_args = number_input(f"Введите количество аргументов для {func_n}-ой булевой функции: ")
        print("Введите значения 0 или 1.")
        n_st = 2 ** n_args #количество строк в ТИ
        bf = [[] for _ in range(n_args)]
        for i in range(n_args):
            st = 2 ** i
            a = [0] * st + [1] * st
            bf[i] = a * (n_st // (2 * st)) # определяет чередование 0 и 1
        boolean_functions.append(bf) #ТИ для n_args аргументов
        values = [] # вспомогательный массив значений векторов
        print("Заполните таблицу истинности, введя значения векторов. Будьте внимательны-принимаются только значения 0 и 1")
        for i in range(n_st):
            print("Значение вектора: ", end='')
            for j in range(n_args):
                print(bf[n_args - 1 - j][i], end=' ')
            values.append(args_input())

        boolean_values.append(values) #массив со значениями векторов всех  функций

    return boolean_values


def class_t0(value):
    return int(value[0] == 0)


def class_t1(value):
    return int(value[-1] == 1)


def class_m(value):
    return int(value == sorted(value))


def class_s(value):
    mid = len(value) // 2
    return int(all((value[i] != value[-i - 1]) for i in range(mid)) and value.count(0) == value.count(1))


def class_l(value):
    n = len(value) -1
    for _ in range(n):
        value = [(value[j]+value[j+1])%2 for j in range(len(value) - 1)] # в массив записываем значения последовательных операций XOR, производимых над вектором значений
        print(value)
        if value[0] == 1:
            return False
    return True



def pfn(post):
    for i in range(5):
        s = sum(post[j][i] for j in range(len(post)))
        if s == len(post):
            return True
    return False


def main():
    boolean_values = get_boolean_values()

    post = []
    for i, value in enumerate(boolean_values):
        in_post = [class_t0(value), class_t1(value), class_m(value), class_s(value), class_l(value)]
        for i, class_func in enumerate(["классу T0", "классу T1", "классу монотоности", "классу самодвойственности", "классу линейности"]):
            print(f"Булева функция номер {i+1} {'не ' if in_post[i] == 0 else ''}принадлежит к {class_func}")
        post.append(in_post)
        print()


    post_or_not = 1
    if len(post) == 1:
        print("В этом наборе всего одна функция, Полный Функциональный Набор нельзя построить из одной функции")
    else:
        for i in range(5):
            s = 0
            for j in range(len(post)):
                if post[j][i] == 1:
                    s += 1
            if s == len(post):
                post_or_not = 0
        if post_or_not == 1:
            print("Введенный набор функций является Полным Функциональным Набором")
        else:
            print("Введенный набор функций не является Полным Функциональным Наборм")
    print()




if __name__ == "__main__":
    main()

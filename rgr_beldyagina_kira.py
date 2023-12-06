#Бельдягина Кира 1 курс инфохимия ису 408254

def is_int() -> int:
    while True:
        value = input()
        if value.isdigit() and int(value) > 0:
            return int(value)
        else:
            print('Некорректный ввод! Введите натуральное число...')
        
def is_bv() -> int:
    while True:
        value = input()
        if value.isdigit():
            match value:
                case '0':
                    return int(value)
                case '1':
                    return int(value)
                case _:
                    print('Некорректный ввод! Введите 0 или 1...')
        else:
            print('Некорректный ввод! Введите 0 или 1...')
    
def check_t0(x:list) -> int:
    return 1 if x[0] == 0 else 0

def check_t1(x:list) -> int:
    return 1 if x[-1] == 1 else 0

def check_m(x:list) -> int:
    return 1 if x == x.sort() else 0

def check_s(x:list) -> int:
    for i in range(int(len(x)/2)):
        if (x[i]==1 and x[len(x)-1-i]==0) or (x[i]==0 and x[len(x)-1-i]==1):
            if x.count(0) == x.count(1):
                return 1
    return 0

def check_l(x:list,all_bf:list, number:int) -> int:
    a = []
    this_f = all_bf[number]
    v_1 = x 

    for i in range(len(x)-1):
        b = []
        for j in range(len(x) - 1 - i):
            b.append((v_1[j]+v_1[j+1])%2)
        a.append(b)
        v_1 = b

    for i in range(len(a)):
        if a[i][0] == 1:
            counter = 0
            for j in range(len(this_f)):
                if this_f[j][i+1] == 1:
                    counter += 1
            if counter > 1:
                return 0
    return 1

def result(i:int, a:int, clas:str) -> None:
    if a == 0:
        print(f"Булева функция #{i+1} не принадлежит {clas}")
    else:
        print(f"Булева функция #{i+1} принадлежит {clas}")

if __name__ == '__main__':
    all_values = []
    all_bf = []
    print("Введите количество БФ будет в наборе: ", end='')
    
    quan_func = is_int() 

    for i in range(1, int(quan_func) + 1):
        print(f"Введите сколько аргументов у {i} булевой функциu будет в наборе: ", end='')
        quan_arg = is_int() 

        print("Далее будут представлены аргументы функции, введите значения (0 или 1)")
        quan_st = 2 ** quan_arg 
        bf = [] * quan_arg
        for j in range(quan_arg): 
            mult = 2 ** j
            a = []
            len_st = 0
            while(len_st != quan_st):
                for j in range(mult):
                    a.append(0)
                    len_st += 1
                for j in range(mult):
                    a.append(1)
                    len_st += 1
            bf.append(a)
        all_bf.append(bf)

        values = []
        for i in range(quan_st): 
            print("Значение для данного вектор ", end='')
            for j in range(quan_arg):
                print(bf[quan_arg-1-j][i], end=' ')
            print("- ", end='')
            value = is_bv()
            print()
            values.append(value)
        all_values.append(values)

    post = []

    for i in range(quan_func):
        s_p = []
        s_p.append(check_t0(all_values[i]))
        s_p.append(check_t1(all_values[i]))
        s_p.append(check_m(all_values[i]))
        s_p.append(check_s(all_values[i]))
        s_p.append(check_l(all_values[i], all_bf, i))
        result(i, s_p[0], "классу T0")
        result(i, s_p[1], "классу T1")
        result(i, s_p[2], "классу монотоности")
        result(i, s_p[3], "классу самодвойственности")
        result(i, s_p[4], "классу линейности")
        post.append(s_p)
        print()

    post_or_not = 1
    if len(post) == 1:
        print("В этом наборе всего одна функция, полный функциональный набор нельзя построить из одной функции")
    else:
        for i in range(5):
            s = 0
            for j in range(len(post)):
                if post[j][i]==1:
                    s+=1
            if s == len(post):
                post_or_not = 0
        if post_or_not == 1:
            print("Введенный набор функций является полным функциональным набором")
        else:
            print("Введенный набор функций не является полным функциональным набором")
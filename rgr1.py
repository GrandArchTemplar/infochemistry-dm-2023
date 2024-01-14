print('Введите количество функций:')
n = input()
# T0, T1, S, M, L
ans = [0] * 5
pack = []
while not(n.isdigit()) or (n[:1] == '0' and len(n) > 1):
    print('Пожалуйста, введите целое число не меньше 0')
    n = input()
else:
    n = int(n)
if n == 0:
    print('Набор из 0 формул не является полным.')
else:
    for i in range(n):
        print('Введите таблицу истинности для', i + 1, 'формулы:')
        s = input()
        c = 0
        l = True
        while 2 ** c < len(s):
            c += 1
        if 2 ** c > len(s):
            l = False
        while s.count('0') + s.count('1') != len(s) or not(l):
            print('Введите корректную таблицу истинности длины 2^n,'
                  '\nсостояящую из 0 и 1')
            s = input()
            c = 0
            l = True
            while 2 ** c < len(s):
                c += 1
            if 2 ** c > len(s):
                l = False
        else:
            pack.append(s)

            # T0, T1, S, M, L
            func = ['-'] * 5

            # T0
            if s[0] == '0':
                func[0] = '+'

            # T1
            if s[-1] == '1':
                func[1] = '+'

            # S
            t = True
            for i in range(len(s) // 2):
                if s[i] == s[-i - 1]:
                    t = False
                    break
            if t:
                func[2] = '+'

            # M
            t = True
            for i in range(len(s)):
                for j in range(len(s)):
                    mi = min(i, j)
                    ma = max(i, j)
                    if ma & mi == mi:
                        if s[ma] < s[mi]:
                            t = False
            if t:
                func[3] = '+'

            # L
            t = True
            twos = [2 ** i for i in range(c + 1)]
            kf = list(map(int, list(s)))
            poly = [kf[0]]
            for i in range(len(kf) - 1):
                newf = []
                for j in range(len(kf) - 1):
                    newf.append((kf[j] + kf[j + 1]) % 2)
                kf = newf[:]
                poly.append(kf[0])
            for i in range(len(poly)):
                if poly[i] == 1 and i not in twos:
                    t = False
            if t:
                func[4] = '+'

            # вывод классов Поста для формулы
            print('Классы Поста для формулы ' + s + ':')
            print('T0 T1 S  M  L')
            print('  '.join(func))

            # вклад в набор
            for i in range(5):
                if func[i] == '-':
                    ans[i] = 1
    print('Набор, состоящий из', n, 'формул:')
    for i in range(n):
        print(str(i + 1) + '.', pack[i])
    if 0 in ans:
        print('Не является полным.')
    else:
        print('Является полным.')
# биномиальный коэффициент
def comb(n, k):
    c = 1
    for i in range(n):
        c *= (i + 1)
    for i in range(k):
        c //= (i + 1)
    for i in range(n - k):
        c //= (i + 1)
    return c

# функция, раскрывающая скобку
def binom(num1, var1, comp1, num2, var2, comp2, exp):
    ans = ''
    for i in range(exp + 1):
        # все i
        allcomp = comp1 * (exp - i) + comp2 * i

        # коэффициент
        coef = comb(exp, i) * (num1 ** (exp - i) * num2 ** i)

        # вычисление знака и комплексной части
        sign = 1
        if coef < 0:
            sign *= -1
        if coef == int(coef):
            coef = abs(int(coef))
        if coef == 0:
            coef = ''
        addi = 0
        if allcomp % 4 == 1:
            addi = 1
        elif allcomp % 4 == 2:
            addi = 0
            sign *= -1
        elif allcomp % 4 == 3:
            addi = 1
            sign *= -1

        # применение знака
        if ans == '':
            if sign == -1:
                ans += '-'
        elif sign == -1:
            ans += '- '
        else:
            ans += '+ '

        # добавление слагаемого
        ans += str(coef) + 'i' * addi + var1 * (exp - i) + var2 * i + ' '

    # вывод ответа
    print(ans)


# ввод
formula = input()[1:-1].split()
exp = int(input())

# первое слагаемое
var1 = formula[0][-1]
if 'i' in formula[0]:
    comp1 = 1
    num1 = float(formula[0][:-2])
else:
    comp1 = 0
    num1 = float(formula[0][:-1])

# второе слагаемое
var2 = formula[2][-1]
if 'i' in formula[2]:
    comp2 = 1
    num2 = float(formula[2][:-2])
else:
    comp2 = 0
    num2 = float(formula[2][:-1])
if formula[1] == '-':
    num2 *= -1

# раскрытие скобки
binom(num1, var1, comp1, num2, var2, comp2, exp)
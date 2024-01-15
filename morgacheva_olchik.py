def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))


def sochet(a, b):
    c = b - a
    m = factorial(b)/(factorial(a)*factorial(c))
    return m


s = str(input("Введите выражение:"))
n = int(input("ВВеедите степень:"))
i = 0
m = ""
while s[i] in "0123456789.,":
    if s[i] == ",":
        m += "."
    else:
        m += s[i]
    i += 1
first = s[i]
i += 1
if s[i] == " ":
    i += 1
i += 1
if s[i] == " ":
    i += 1
d = ""
while s[i] in "0123456789.,":
    if s[i] == ",":
        d += "."
    else:
        d += s[i]
    i += 1
second = s[i]
if first == second:
    res1 = (int(m) + int(d))**n
    res2 = n*first
    print("Результат: " + str(res1) + res2)
else:
    res = ""
    for i in range(n+1):
        if i != n:
            res += " " + (str(sochet(i, n)*(float(m)**(n-i) * float(d)**i)) + (n-i)*first + i*second)
            res += " +"
        else:
            res += " " + (str(sochet(i, n)*(float(m)**(n-i) * float(d)**i)) + (n-i)*first + i*second)
print(res)


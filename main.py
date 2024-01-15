def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)



def sochet(a, b):
    c = b - a
    m = factorial(b)/(factorial(a)*factorial(c))
    return m


s = str(input("Введите выражение:"))
n = int(input("ВВеедите степень:"))
i = 0
m = ""
if s[0] == "-":
    gr = "-"
    s = s[1:]
if s[0] not in "123456789":
    m = 1
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
znak = s[i]
i += 1
if gr == "-":
    m = -int(m)
if s[i] == " ":
    i += 1
d = ""
if s[i] not in "123456789":
    d = 1
while s[i] in "0123456789.,":
    if s[i] == ",":
        d += "."
    else:
        d += s[i]
    i += 1
second = s[i]
if znak == "-":
    d = -int(d)
print(d)
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


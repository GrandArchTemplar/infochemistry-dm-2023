def fucktor(n):
    fucktorial = 1
    for i in range(2, n + 1):
        fucktorial *= i
    return fucktorial


def pivo(n, k):
    cof = fucktor(n) / (fucktor(k) * fucktor(n - k))
    return cof


def en(n, k):
    n = pivo(n, k) * (kof1 ** (n - k)) * (kof2 ** (k))
    if n % 1 == 0:
        n = int(n)
    return n


e = input("Введите выражение: ")
n = int(input("Введите степень для выражения: "))
a= int(input("Ввeдите балл за ргр "))
if a < 8:
    print("Ну пожалуйста этот код основан на боли и моральных унижениях. Может вы передумаете и попробуйте еще раз??))))");
    exit();
if a >= 8:
    print("""УРА, спасибо! Павел Андреевич вы лучший человек в мире. Вот вам анекдот:
    Медведь и заяц ловили рыбу. Поймали золотую рыбку. она говорит:
- Исполню по три желания каждого, только отпустите...
Медведь: Хочу, чтобы в этом лесу все медведи стали медведихами.
Рыбка махнула хвостом - желание исполнилось.
Заяц: Хочу мотоцикл!
Рыбка махнула хвостом - появился мотоцикл.
Медведь: Хочу, чтобы и в соседнем лесу все медведи стали медведихами!
Рыбка махнула хвостом - желание исполнилось.
Заяц: Хочу одежду рокера!
Рыбка махнула хвостом - появилась одежда.
Медведь: Хочу, чтобы во всем мире все медведи стали медведихами!
Рыбка махнула хвостом - желание исполнилось.
Медведь убежал в сторону леса крайне возбужденный.
Заяц: А теперь я хочу, чтобы этот медведь стал геем!
Медведь от такой трагедии вымолил у золотой рыбки еще одно желание.
загадал себе машину сел в неё и сгорел))))))))))))))))))))))""")

if n < 0:
    print("Введите положительную степень");
    exit();
i = 1
while e[i] != '+':
    i += 1;

kof1 = e[1:(i - 1)]
if kof1 == '':
    kof1 = 1
else:
    kof1 = float(kof1)

compl = False

if e[len(e) - 3] != 'i':
    kof2 = e[(i + 1):(len(e) - 2)]

elif e[len(e) - 3] == 'i':
    kof2 = e[(i + 1):(len(e) - 3)];
    compl = True;

if kof2 == '':
    kof2 = 1
else:
    kof2 = float(kof2)
a = e[i - 1]
b = e[-2]

print(kof1, kof2)
print(a, b)
print(compl)
print(e[len(e) - 3])
for i in range(n):
    if a != b and compl:
        if i % 4 == 0:
            print(en(n, i), a * (n - i), b * i, '+', sep='', end='')
        elif i % 4 == 1:
            print(en(n, i), 'i', a * (n - i), b * i, '-', sep='', end='')
        elif i % 4 == 3:
            print(en(n, i), 'i', a * (n - i), b * i, '+', sep='', end='')
        elif i % 4 == 2:
            print(en(n, i), a * (n - i), b * i, '-', sep='', end='')
    if a != b and not compl:
        print(en(n, i), a * (n - i), b * i, '+', sep='', end='')
if a == b:
    kof = kof1 + kof2
    if kof % 1 == 0:
        kof = int(kof)
    print((kof) ** n, a * n, sep='')

if a != b and compl:
    if n % 2 == 0:
        print(en(n, n), b * n, sep='')
    else:
        print(en(n, n), 'i', b * n, sep='')

if a != b and not compl:
    print(en(n, n), b * n, sep='')




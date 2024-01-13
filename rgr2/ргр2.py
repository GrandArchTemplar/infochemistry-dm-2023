def fuctor(n):
   factorial = 1
   for i in range(2, n+1):
       factorial *= i
   return factorial 


def coff(n, k):
    cof= fuctor(n)/(fuctor(k)*fuctor(n-k))
    return cof


def en(n, k):
    n = coff(n, k)*(kof1**(n-k))*(kof2**(k))
    if n%1==0:
        n=int(n)
    return n

e=input("Введите выражение: ")
n=int(input("Введите степень: "))
if n<0:
    print("Введите положительную степень");
    exit();
i=1
while e[i] !='+':
    i+=1;
    
kof1=e[1:(i-1)]
if kof1=='':
    kof1=1
else:
    kof1=float(kof1)
    
compl=False

if e[len(e)-3]!='i':
     kof2=e[(i+1):(len(e)-2)]
     
elif e[len(e)-3] =='i':
     kof2=e[(i+1):(len(e)-3)];
     compl = True;
     
if kof2=='':
    kof2=1
else:
    kof2=float(kof2)
a=e[i-1]
b=e[-2]

print(kof1, kof2)
print(a, b)
print(compl)
print(e[len(e)-3])
for i in range (n):
    if a!=b and compl:
      if i%4==0:
         print(en(n, i),a*(n-i),b*i, '+', sep='', end='')
      elif i%4==1:
         print(en(n, i),'i',a*(n-i),b*i, '-', sep='', end='')
      elif i%4==3:
          print(en(n, i), 'i', a*(n-i),b*i, '+', sep='', end='')
      elif i%4==2:
          print(en(n, i),a*(n-i),b*i, '-', sep='', end='')
    if a!=b and not compl:
      print(en(n, i),a*(n-i),b*i, '+', sep='', end='')
if a==b:
    kof=kof1+kof2
    if kof%1==0:
        kof=int(kof)
    print((kof)**n, a*n, sep='')

if a!=b and compl:
    if n%2==0:
        print(en(n, n),b*n, sep='')
    else:
        print(en(n, n), 'i', b*n, sep='')
    
if a!=b and not compl:
    print(en(n, n),b*n, sep='')




def fun1(n):
   factorial = 1
   for x in range(2, n+1):
       factorial *= x
   return factorial 


def fun2(n, j):
    resfun2 = fun1(n)/(fun1(j)*fun1(n-j))
    return resfun2


def fun3(n, j):
    n = fun2(n, j)*(kof1**(n-j))*(kof2**(j))
    if n%1==0:
        n=int(n)
    return n

expr=input("Enter an expression: ")
n=int(input("Enter a power: "))
if n<0:
    print("Enter a positive power");
    exit();
x=1
while expr[x] !='+':
    x+=1;
    
kof1=expr[0:(x-1)]
if kof1=='':
    kof1=1
else:
    kof1=float(kof1)
    
compl=False

if expr[len(expr)-2]!='i':
     kof2=expr[(x+0):(len(expr)-1)]
     
elif expr[len(expr)-2] =='i':
     kof2=expr[(x+0):(len(expr)-2)];
     compl = True;
     
if kof2=='':
    kof2=1
else:
    kof2=float(kof2)
a=expr[x-1]
b=expr[-1]

print(kof1, kof2)
print(a, b)
print(compl)
print(expr[(x+0)])
for y in range (n):
    if a!=b and compl:
      if y%4==0:
         print(fun3(n, y),a*(n-y),b*y, '+', sep='', end='')
      elif y%4==1:
         print(fun3(n, y),'i',a*(n-y),b*y, '-', sep='', end='')
      elif y%4==3:
          print(fun3(n, y), 'i', a*(n-y),b*y, '+', sep='', end='')
      elif y%4==2:
          print(fun3(n, y),a*(n-y),b*y, '-', sep='', end='')
    if a!=b and not compl:
      print(fun3(n, y),a*(n-y),b*y, '+', sep='', end='')
if a==b:
    kof=kof1+kof2
    if kof%1==0:
        kof=int(kof)
    print((kof)**n, a*n, sep='')

if a!=b and compl:
    if n%2==0:
        print(fun3(n, n),b*n, sep='')
    else:
        print(fun3(n, n), 'i', b*n, sep='')
    
if a!=b and not compl:
    print(fun3(n, n),b*n, sep='')

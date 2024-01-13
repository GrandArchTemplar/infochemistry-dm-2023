def forme(e):
    e = str(e)
    col=math.ceil(math.log2(len(e)))
    row=len(e)
    table = []
    for i in range(row):
        v = [int(r) for r in bin(i)[2:].zfill(col)]
        drow = [j for j in list(zip([v], [[int(e[i])]]))][0]
        r = []
        for i in drow:
            r.extend(i)
        table.append(r)
    return table
#---------------------принадлежность Т0------------------------
def is_T0(e):
        if e[0] == '0':
            return 1;
        else:
            return 0
   

#---------------------принадлежность Т1------------------------
def is_T1(e):
        if e[-1] == '1':
            return 1;
        else:
            return 0


#---------------------принадлежность М------------------------
def is_M(e):
    
    for i in range(0,len(e)-1):
        for j in range(i+1, len(e)):
            if (i&j)==i and (int(e[i])>int(e[j])): 
                        return 0
        return 1


#---------------------принадлежность S------------------------
def is_S(e):
    new_e=str(e[::-1]).replace("1", "-").replace("0", "1").replace("-", "0")
    if e== new_e:
        return 1
    else:
        return 0




#---------------------принадлежность L------------------------

def is_L(e):
    formtable = forme(e)
    table = [[]]
    for i in formtable:
        if i[:-1].count(1) == 1:
            table.append(i)
    table = table[1:]
    a= [0]*(len(table[0][:-1])+1)
    a[0]=formtable[0][-1]
    for i in range(0, len(table[0][:-1])):
        a[len(table[0][:-1])-i]=a[0]^table[i][-1]
    new= [a[0]]*len(e)
    for i in range(1, len(formtable)):
        for j in range(len(formtable[i][:-1])):
            new[i]^=formtable[i][j]*a[j+1]
    e = str(e)
    str_new = ""
    for i in new:
        str_new+=str(i)
    new = str_new
    if new == e:
        return 1
    else:
        return 0

#-------------------------------------------------------------    
def is_binary(e):
    binary_digits = {'0', '1'}
    number_digits = set(e)
    if number_digits.issubset(binary_digits):
        return False
    else:
        return True


#-------------------------------------------------------------
import math
import random
n = int(input("Введите количество функций: "))
setf = []
for i in range(n):
    a=input("Введите функцию: ");
    j=1
    while j<len(a):
        j=j*2
    if (j!=len(a)) or (int(a)<0) or is_binary(a):
        print('Введите корректные данные');
        exit();
    setf.insert(i,a);

T0=[]
T1=[]
S=[]
M =[]
L=[]

for i in range(n):
    T0.append(is_T0(setf[i]));
    T1.append(is_T1(setf[i]));
    M.append(is_M(setf[i]));
    S.append(is_S(setf[i]));
    L.append(is_L(setf[i]));
    
print(setf)
print('T0 ', T0)
print('T1 ', T1)
print('M ', M)
print('S ', S)
print('L ', L)
if ('0' in T0) and ('0' in T1) and ('0' in M) and ('0' in S) and ('0' in L):
    print("Набор полный")
else:
    print("Набор неполный")

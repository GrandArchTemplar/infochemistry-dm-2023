def fun1(t):
    t = str(t)
    column=math.ceil(math.log2(len(t)))
    line=len(t)
    table = []
    for x in range(line):
        q = [int(p) for p in bin(x)[2:].zfill(column)]
        aline = [y for y in list(zip([q], [[int(t[x])]]))][0]
        p = []
        for x in aline:
            p.extend(x)
        table.append(p)
    return table
#class T0
def class_t0(t):
        if t[0] == '0':
            return 1;
        else:
            return 0


#class T1
def class_t1(t):
        if t[-1] == '1':
            return 1;
        else:
            return 0


#monotonicity class
def class_m(t):
    
    for x in range(0,len(t)-1):
        for y in range(x+1, len(t)):
            if (x&y)==x and (int(t[x])>int(t[y])):
                        return 0
        return 1


#self-duality class
def class_s(t):
    new_t=str(t[::-1]).replace("1", "-").replace("0", "1").replace("-", "0")
    if t== new_t:
        return 1
    else:
        return 0




#polynomial linearity class

def class_l(t):
    formtable = fun1(t)
    table = [[]]
    for x in formtable:
        if x[:-1].count(1) == 1:
            table.append(x)
    table = table[1:]
    b= [0]*(len(table[0][:-1])+1)
    b[0]=formtable[0][-1]
    for x in range(0, len(table[0][:-1])):
        b[len(table[0][:-1])-x]=b[0]^table[x][-1]
    new= [b[0]]*len(t)
    for x in range(1, len(formtable)):
        for y in range(len(formtable[x][:-1])):
            new[x]^=formtable[x][y]*b[y+1]
    t = str(t)
    str_new = ""
    for x in new:
        str_new+=str(x)
    new = str_new
    if new == t:
        return 1
    else:
        return 0

#########################################################################
def if_binary(t):
    binary_digits = {'0', '1'}
    number_digits = set(t)
    if number_digits.issubset(binary_digits):
        return False
    else:
        return True


########################################################################
import math
import random
n = int(input("Enter the number of functions: "))
setf = []
for x in range(n):
    b=input("Enter the function: ");
    y=1
    while y<len(b):
        y=y*2
    if (y!=len(b)) or (int(b)<0) or if_binary(b):
        print('Please, enter a correct function');
        exit();
    setf.insert(x,b);

T0=[]
T1=[]
S=[]
M =[]
L=[]

for x in range(n):
    T0.append(class_t0(setf[x]));
    T1.append(class_t1(setf[x]));
    M.append(class_m(setf[x]));
    S.append(class_s(setf[x]));
    L.append(class_l(setf[x]));
    
print(setf)
print('T0 ', T0)
print('T1 ', T1)
print('M ', M)
print('S ', S)
print('L ', L)
if ('0' in T0) and ('0' in T1) and ('0' in M) and ('0' in S) and ('0' in L):
    print("The set is complete")
else:
    print("The set is incomplete")

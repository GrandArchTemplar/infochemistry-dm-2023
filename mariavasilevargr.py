####number of functions input button####
def click_button():
    global count
    x=int(entry.get())
    #foolproof
    if x==0 or x<0:
        label1=Label(window, text="Enter x>0!", width=45, height=5, bg="#000000", fg="red", font=("Algerian", 18))
        label1.pack()
        count+=1
        if count == 1:
            label1.destroy()
            count = 0
            #if the correct number is entered
    else:
        window.destroy()
        window1=Tk()
        window1.configure(bg="#000000")
        label1=Label(window1, text="Enter functions in the form of truth tables:", width=65, height=5, bg="#000000", fg="red",font=("Algerian", 18))
        label1.pack()
        #generating function input fields
        for t in range(0,x):
            label2=Label(window1, text=f'Enter function {t+1}:',fg="black", bg="#FF0000", font="Algerian")
            label2.pack(anchor="center",padx=230)
            entry1=Entry(window1,bg="#FF0000")
            entry1.pack(anchor="center")
            A.append(entry1)
        btn1=Button(window1,text="Enter",command=click_button1,bg="#FF0000", fg="black", font="Algerian")
        btn1.pack()
def click_button1():
    for t in range(0,len(A)):
        C.append(list(A[t].get()))
        B.append(list(A[t].get()))
    #checking the number of elements (power of two)
    for t in range(0,len(A)):
        a=math.log(len(B[t]),2)
    #check, only zeros and ones
    for t in range(0,len(A)):
        for y in range(0,len(B[t])):
            if int(B[t][y])!=0 and int(B[t][y])!=1:
                window4=Tk()
                window4.configure(bg="#000000")
                label3=Label(window4, text="Incorrect vector shapes entered, try again", width=65, height=5, bg="#000000", fg="red",font=("Algerian", 18))
                label3.pack()
                break

####post classes####
        #self-duality class
    for t in range(0,len(A)):
        for y in range(0,len(B[t])//2):
            global summ
            global Sam
            #checking opposite values
            if (int(B[t][y])+int(B[t][len(B[t])-(y+1)]))==1:
                summ+=1
        if summ==(len(B[t])//2):
            Sam.append(1)
            summ=0
        else:
            Sam.append(0)
            summ=0
    print('S',Sam,sep='  ')
    #class T0
    for t in range(0,len(A)):
        if int(B[t][0])==0:
            T0.append(1)
        else:
            T0.append(0)
    print('T0',T0)
    #class T1
    for t in range(0,len(A)):
        if int(B[t][len(B[t])-1])==0:
            T1.append(0)
        else:
            T1.append(1) 
    print('T1',T1)
    #monotonicity class
    for t in range(0,len(A)):
        c=(''.join(str(o) for o in (B[t])))
        d=int(math.log(len(B[t]),2))
        def Monoton(c,d):
            p=2**d
            for k in range(0,p-1):
                for y in range(k+1,p):
                    if (k&y)==k and int(B[t][k])>int(B[t][y]):
                        return 0
            return 1
        M.append(Monoton(c,d))
    print('M',M, sep='  ')
    #polynomial linearity class
#Zhegalkin polynomial
    for t in range(0,len(A)):
        global b
        for k in range(0,len(B[t])):
            b+=1
            for y in range(len(B[t])-1,b,-1):
                B[t][y]=(int(B[t][y-1])+int(B[t][y]))%2
    for t in range(0,len(A)):
        D=[]
        global summ2
        if summ2==0:
            L.append(1)
            summ2=0
            summ1=0
        else:
            L.append(0)
            summ2=0        
        #binary system, sum the values from the table
        for y in range(0,len(B[t])):
            if int(B[t][y])==1:
                D.append(bin(y)[2:])
        for k in range(0,len(D)):
            D[k]=list(D[k])
        for y in range(0,len(D)):
            summ1=0
            summ2=0
            for k in range(0,len(D[y])):
                summ1+=int(D[y][k])
            if summ1>1:
                summ2+=1
                break
    print('L',L,sep='  ')
    for t in range(0,len(T0)):
        global summT0
        summT0+=T0[t]
    for t in range(0,len(T1)):
        global summT1
        summT1+=T1[t] 
    for t in range(0,len(M)):
        global summM
        summM+=M[t]
    for t in range(0,len(L)):
        global summL
        summL+=L[t]
    for t in range(0,len(Sam)):
        global summSam
        summSam+=Sam[t]    
    if summT0<len(A) and summT1<len(A) and summM<len(A) and summL<len(A) and summSam<len(A):
        print('The set is complete')
    else:  
        print('The set is incomplete')
####variables####
A=[]
B=[]
C=[]
D=[]
summ=0
summ1=0
summ2=0
summT0=0
summT1=0
summM=0
summL=0
summSam=0
T0=[]
T1=[]
M=[]
Sam=[]
L=[]
count=0
b=-1
####start window####
import math
from tkinter import *
from tkinter import ttk
import sys
window=Tk()
window.configure(bg="#000000")
label=Label(window, text="Enter number of functions:", width=45, height=5, bg="#000000", fg="red", font=("Algerian", 18))
label.pack()
entry=Entry(window, width=35, bg="#FF0000")
entry.pack()
btn=Button(window,text="Enter",command=click_button,bg="#000000", fg="red", font=("Algerian"))
btn.pack()
window.mainloop()
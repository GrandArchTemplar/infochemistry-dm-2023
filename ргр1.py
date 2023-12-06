#кнопка ввода кол-ва функций
def click_button():
    global count
    n=int(entry.get())
    
    
    #защита от дурака

    
    if n==0 or n<0:
        if count==1:
            label1.destroy()
            count=0        
        label1=Label(window, text="Введите n>0!", width=80, height=7, bg="#BAD1CD", fg="black",font="20") 
        label1.pack()
        count+=1

        
    #если введено корректное число

        
    else:
        window.destroy()
        window1=Tk()
        window1.configure(bg="#EBD5D5")
        label1=Label(window1, text="Введите ваши функции в виде таблиц истинности:", width=80, height=7, bg="#F9F9F9", fg="black",font="20")
        label1.pack()


        
        #генерация введенного числа полей ввода функций


        
        for i in range(0,n):
            label2=Label(window1, text=f'Введите функцию {i+1}:',bg="#EBD5D5")
            label2.pack(anchor="nw",padx=230)
            entry1=Entry(window1,bg="#EBD5D5")
            entry1.pack(anchor="center")
            A.append(entry1)
        btn1=Button(window1,text="Ввод",command=click_button1,bg="#F9F9F9")
        btn1.pack()
def click_button1():
    global schet
    for i in range(0,len(A)):
        C.append(list(A[i].get()))
        B.append(list(A[i].get()))

        
    #проверка на дурака, ничего, кроме функции внести нельзя 0_0 (прооверка числа элементов, это всегда степень двойки)

        
    for i in range(0,len(A)):
        a=math.log(len(B[i]),2)

        
    #проверяет целочисленность

        
        if (a.is_integer()==False or a==0.0):
            window4=Tk()
            window4.configure(bg="#F9F9F9")

            label3=Label(window4, text="Введены некоррекные векторные формы, начните заново", width=80, height=7, bg="#F9F9F9", fg="black",font="20")
            label3.pack()
            schet=+1
            break

        
        #проверка, что ввели только нули и единицы

        
    for i in range(0,len(A)):
        for j in range(0,len(B[i])):
            if int(B[i][j])!=0 and int(B[i][j])!=1 and schet!=1:
                window4=Tk()
                window4.configure(bg="#F9F9F9")
                label3=Label(window4, text="Введены некоррекные векторные формы, начните заново", width=80, height=7, bg="#F9F9F9", fg="black",font="20")
                label3.pack()
                break

            
        #начем с класса самодвойственности, в цикле питон глупенький и забывает все переменные, а global ищет их по всему коду

            
    for i in range(0,len(A)):
        for j in range(0,len(B[i])//2):
            global summ
            global Sam

            
            #здесь мы проверяем противоположные значения

            
            if (int(B[i][j])+int(B[i][len(B[i])-(j+1)]))==1:
                summ+=1
        if summ==(len(B[i])//2):
            Sam.append(1)
            summ=0
        else:
            Sam.append(0)
            summ=0
    print('S',Sam,sep='  ')

    
    #класс T0

    
    for i in range(0,len(A)):
        if int(B[i][0])==0:
            T0.append(1)
        else:
            T0.append(0)
    print('T0',T0)

    
    #класс T1

    
    for i in range(0,len(A)):
        if int(B[i][len(B[i])-1])==0:
            T1.append(0)
        else:
            T1.append(1) 
    print('T1',T1)

    
    #класс монотонности

    
    for i in range(0,len(A)):
        c=(''.join(B[i]))
        d=int(math.log(len(B[i]),2))
        def Monoton(c,d):
            p=2**d
            for k in range(0,p-1):
                for j in range(k+1,p):
                    if (k&j)==k and int(B[i][k])>int(B[i][j]):
                        return 0
            return 1
        M.append(Monoton(c,d))
    print('M',M, sep='  ')

    
    #класс линейности полинома

    
#находим полином жегалкина
    
    for i in range(0,len(A)):
        global b
        for k in range(0,len(B[i])):
            b+=1
            for j in range(len(B[i])-1,b,-1):
                B[i][j]=(int(B[i][j-1])+int(B[i][j]))%2
    for i in range(0,len(A)):
        D=[]
        global summ2
        if summ2==0:
            L.append(1)
            summ2=0
            summ1=0
        else:
            L.append(0)
            summ2=0

            
        #перевела в двоичную, чтобы соотнести полином Жегалкина с таблицей истинности, суммирую значения из таблицы, т.к. если сумма больше 1, то полином нелинейный

            
        for j in range(0,len(B[i])):
            if int(B[i][j])==1:
                D.append(bin(j)[2:])
        for k in range(0,len(D)):
            D[k]=list(D[k])
        for j in range(0,len(D)):
            summ1=0
            summ2=0
            for k in range(0,len(D[j])):
                summ1+=int(D[j][k])
            if summ1>1:
                summ2+=1
                break
    print('L',L,sep='  ')

    window = Tk()
    window.title("Классификация функций")


# Вывод результатов


    for i in range(0, len(A)):
        label1 = Label(window, text="S - " + str(Sam[i]), width=80, height=2, bg="#E3E3E3", fg="black",font="20")
        label1.pack()
        label2 = Label(window, text="T0 - " + str(T0[i]), width=80, height=2, bg="#E3E3E3", fg="black",font="20")
        label2.pack()
        label3 = Label(window, text="T1 - " + str(T1[i]), width=80, height=2, bg="#E3E3E3", fg="black",font="20")
        label3.pack()
        label4 = Label(window, text="M - " + str(M[i]), width=80, height=2, bg="#E3E3E3", fg="black",font="20")
        label4.pack()
        label5 = Label(window, text="L - " + str(L[i]), width=80, height=2, bg="#E3E3E3", fg="black",font="20")
        label5.pack()
    for i in range(0,len(T0)):
        global summT0
        summT0+=T0[i]
    for i in range(0,len(T1)):
        global summT1
        summT1+=T1[i] 
    for i in range(0,len(M)):
        global summM
        summM+=M[i]
    for i in range(0,len(L)):
        global summL
        summL+=L[i]
    for i in range(0,len(Sam)):
        global summSam
        summSam+=Sam[i]
    if summT0<len(A) and summT1<len(A) and summM<len(A) and summL<len(A) and summSam<len(A):
        label6 = Label(window, text="Набор является полным", width=80, height=1, bg="#E3E3E3", fg="black",font="20")
        label6.pack()
    else:  
        label6 = Label(window,text="Набор является неполным", width=80, height=1, bg="#E3E3E3", fg="black",font="20")
        label6.pack()

# Закрытие окна


    window.mainloop()
    

        
#все необходимые переменные

        
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
schet=0


#начальное окно


import math
from tkinter import *
from tkinter import ttk
import sys
window=Tk()
window.configure(bg="#C8D9EB")
label=Label(window, text="Введите количество булевых функций:", width=80, height=7, bg="#E3E3E3", fg="black",font="40")
label.pack()
entry=Entry(window,bg="#D6D1CB")
entry.pack()
btn=Button(window,text="Ввод",command=click_button,bg="#FFF5A5")
btn.pack()
window.mainloop()

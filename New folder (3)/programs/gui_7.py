from functools import partial
from tkinter import *
t=Tk()
t.geometry("400x600")
def add(result,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    res=int(num1)+int(num2)
    result.config(text="result=%d"%res)
    return
number1=StringVar()
number2=StringVar()
result=Label(t)
result.place(x=120,y=170)

name=Label(t,text="A").place(x=30,y=50)
txt1=Entry(t,textvariable=number1).place(x=90,y=50)
Password=Label(t,text="B").place(x=30,y=90)
txt2=Entry(t,textvariable=number2).place(x=90,y=90)
add=partial(add,result,number1,number2)
submit=Button(t,text="ADD",command=add).place(x=120,y=130)
t.mainloop()

from tkinter import *
t=Tk()
t.geometry("400x600")

name=Label(t,text="Name").place(x=30,y=50)
txt1=Entry(t).place(x=90,y=50)
Password=Label(t,text="Password").place(x=30,y=90)
txt2=Entry(t).place(x=90,y=90)
submit=Button(t,text="SUBMIT").place(x=120,y=130)
t.mainloop()

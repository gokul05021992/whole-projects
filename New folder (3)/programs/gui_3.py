from tkinter import *
t=Tk()
t.geometry("200x200")

name=Label(t,text="Name").grid(row=0,column=0)
txt1=Entry(t).grid(row=0,column=1)
Password=Label(t,text="Password").grid(row=1,column=0)
txt2=Entry(t).grid(row=1,column=1)
submit=Button(t,text="SUBMIT").grid(row=2,column=1)
t.mainloop()

from tkinter import *

t=Tk()
t.geometry("200x200")
btn1=Button(t,text="red",fg="red",bg="yellow")
btn1.pack(side=LEFT)
btn2=Button(t,text="blue")
btn2.pack(side=RIGHT)

btn3=Button(t,text="green")
btn3.pack(side=TOP)

btn4=Button(t,text="black")
btn4.pack(side=BOTTOM)

t.mainloop()

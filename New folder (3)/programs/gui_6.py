from tkinter import *
from tkinter import messagebox

t=Tk()
t.geometry("200x200")
checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()
chbtn1=Checkbutton(t,text="c",variable=checkvar1,onvalue=1,offvalue=0,height=2,width=10)
chbtn1.pack()
chbtn2=Checkbutton(t,text="c++",variable=checkvar2,onvalue=1,offvalue=0,height=2,width=10)
chbtn2.pack()
chbtn3=Checkbutton(t,text="java",variable=checkvar3,onvalue=1,offvalue=0,height=2,width=10)
chbtn3.pack()
t.mainloop()

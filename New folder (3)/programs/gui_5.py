from tkinter import *
from tkinter import messagebox

t=Tk()
t.geometry("200x200")
def show():
    messagebox.showinfo("Hello you clicked the button...!")
btn1=Button(t,text="red",fg="red",bg="yellow",command=show)
btn1.pack()
t.mainloop()

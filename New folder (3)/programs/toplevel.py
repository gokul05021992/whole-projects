from tkinter import *

t = Tk()

t.geometry("200x200")


def open():
    top = Toplevel(t)
    top.mainloop()


btn = Button(t, text="open", command=open)

btn.place(x=75, y=50)

t.mainloop()
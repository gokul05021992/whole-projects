from tkinter import *

top = Tk()

top.geometry("200x250")

lbl = Label(top, text="A list of courses available...")

listbox = Listbox(top)

listbox.insert(1, "C")

listbox.insert(2, "C++")

listbox.insert(3, "Java")

listbox.insert(4, "python")

lbl.pack()
listbox.pack()

top.mainloop()
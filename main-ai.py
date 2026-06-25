from tkinter import *
from random import randint

def w():
    t = Tk()
    t.geometry(f"+{randint(0,1000)}+{randint(0,700)}")
    Label(t, text="Закрыть это окно?").pack()
    Button(t, text="Да", command=lambda: w()).pack(side=LEFT)
    Button(t, text="Нет", command=t.destroy).pack(side=RIGHT)

w()
mainloop()
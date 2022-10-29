from tkinter import font
import tk
from tkinter import *
import tkinter as tk

from main import display


win = tk.Tk()
win.geometry("1250x350")
win.title('Exercises')
win.resizable(False, False)


myA = open("files/myA.txt", "w")
myB = open("files/myB.txt", "w")
mySum = open("files/mySum.txt", "w")
myProd = open("files/myProd.txt", "w")


T = [0,0]
A = [        [     ],[     ]      ]
B = [        [     ],[     ]      ]
Sum = [             ]
Prod = [             ]

elemNrA = 0


def win_ex1():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("1200x900")
    newWindow.title('Matricea A')
    newWindow.resizable(False, False)

    text_v = "Afisarea matricii A in forma de lista de liste :"
    txth = ""
    with open('files/myA.txt') as file:
        for line in file:
            txth = txth + (str(line.rstrip()))
            txth = txth + str('\n')
    text_h = (txth)


    scroll_v = Scrollbar(newWindow)
    scroll_v.pack(side=RIGHT, fill="y")

    scroll_h = Scrollbar(newWindow, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")


    text = Text(newWindow, height=1150, width=850, yscrollcommand=scroll_v.set,
                xscrollcommand=scroll_h.set, wrap=NONE, font=('Helvetica 15'))
    text.pack(fill=BOTH, expand=0)
    text.insert(END, '\n')
    text.insert(END, text_v)
    text.insert(END, '\n\n\n')
    text.insert(END, text_h)

    scroll_h.config(command=text.xview)
    scroll_v.config(command=text.yview)


def win_ex2():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("1200x900")
    newWindow.title('Matricea B')
    newWindow.resizable(False, False)

    text_v = "Afisarea matricii B in forma de lista de liste :"
    txth = ""
    with open('files/myB.txt') as file:
        for line in file:
            txth = txth + (str(line.rstrip()))
            txth = txth + str('\n')
    text_h = (txth)


    scroll_v = Scrollbar(newWindow)
    scroll_v.pack(side=RIGHT, fill="y")

    scroll_h = Scrollbar(newWindow, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")


    text = Text(newWindow, height=1150, width=850, yscrollcommand=scroll_v.set,
                xscrollcommand=scroll_h.set, wrap=NONE, font=('Helvetica 15'))
    text.pack(fill=BOTH, expand=0)
    text.insert(END, '\n')
    text.insert(END, text_v)
    text.insert(END, '\n\n\n')
    text.insert(END, text_h)

    scroll_h.config(command=text.xview)
    scroll_v.config(command=text.yview)


def win_ex3():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("1200x900")
    newWindow.title('Matricea A+B')
    newWindow.resizable(False, False)

    text_v = "Afisarea matricii formate din suma A + B :"
    txth = ""
    with open('files/mySum.txt') as file:
        for line in file:
            txth = txth + (str(line.rstrip()))
            txth = txth + str('\n')
    text_h = (txth)


    scroll_v = Scrollbar(newWindow)
    scroll_v.pack(side=RIGHT, fill="y")

    scroll_h = Scrollbar(newWindow, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")


    text = Text(newWindow, height=1150, width=850, yscrollcommand=scroll_v.set,
                xscrollcommand=scroll_h.set, wrap=NONE, font=('Helvetica 15'))
    text.pack(fill=BOTH, expand=0)
    text.insert(END, '\n')
    text.insert(END, text_v)
    text.insert(END, '\n\n\n')
    text.insert(END, text_h)

    scroll_h.config(command=text.xview)
    scroll_v.config(command=text.yview)


def win_ex4():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("1200x900")
    newWindow.title('Matricea A*A')
    newWindow.resizable(False, False)

    text_v = "Afisarea matricii formate din imultirea A * A :"
    txth = ""
    with open('files/myProd.txt') as file:
        for line in file:
            txth = txth + (str(line.rstrip()))
            txth = txth + str('\n')
    text_h = (txth)


    scroll_v = Scrollbar(newWindow)
    scroll_v.pack(side=RIGHT, fill="y")

    scroll_h = Scrollbar(newWindow, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")


    text = Text(newWindow, height=1150, width=850, yscrollcommand=scroll_v.set,
                xscrollcommand=scroll_h.set, wrap=NONE, font=('Helvetica 15'))
    text.pack(fill=BOTH, expand=0)
    text.insert(END, '\n')
    text.insert(END, text_v)
    text.insert(END, '\n\n\n')
    text.insert(END, text_h)

    scroll_h.config(command=text.xview)
    scroll_v.config(command=text.yview)



display()

b1_3 = font.Font(family='Times New Roman', size=30, weight='bold')

b1 = tk.Button(win, text="Matrix \n A", bg='#e35d34', fg='#000000', borderwidth=4, relief='raised',  height=6, width=12, command=win_ex1)
b1['font'] = b1_3
b1.place(relx=0.125, rely=0.5, anchor=CENTER)
b2 = tk.Button(win, text="Matrix \n B", bg='#7bdb63', fg='#000000', borderwidth=4, relief='raised',  height=6, width=12, command=win_ex2)
b2['font'] = b1_3
b2.place(relx=0.375, rely=0.5, anchor=CENTER)
b3 = tk.Button(win, text="Matrix \n A + B", bg='#6397db', fg='#000000', borderwidth=4, relief='raised',  height=6, width=12, command=win_ex3)
b3['font'] = b1_3
b3.place(relx=0.625, rely=0.5, anchor=CENTER)
b4 = tk.Button(win, text="Matrix \n A * A", bg='#ffd257', fg='#000000', borderwidth=4, relief='raised', height=6, width=12, command=win_ex4)
b4['font'] = b1_3
b4.place(relx=0.875, rely=0.5, anchor=CENTER)

win.mainloop()

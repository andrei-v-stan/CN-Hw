from tkinter import font
import tk
from tkinter import *
import tkinter as tk

from main import *


win = tk.Tk()
win.geometry("600x600")
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



def win_ex():

    newWindow = tk.Toplevel(win)
    newWindow.geometry("1200x900")
    newWindow.title('Afisare rezultat')
    newWindow.resizable(False, False)

    text_v = "Rezultatul :"
    txth = ""
    with open('files/x1.txt') as file:
        for line in file:
            txth = txth + (str(line.rstrip()))
            txth = txth + str('\n')
    text_h = (txth)


    scroll_v = Scrollbar(newWindow)
    scroll_v.pack(side=RIGHT, fill="y")

    scroll_h = Scrollbar(newWindow, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")


    text = Text(newWindow, height=850, width=1250, yscrollcommand=scroll_v.set,
                xscrollcommand=scroll_h.set, wrap=NONE, font=('Helvetica 15'))
    text.pack(fill=BOTH, expand=0)
    text.insert(END, '\n')
    text.insert(END, text_v)
    text.insert(END, '\n\n\n')
    text.insert(END, text_h)

    scroll_h.config(command=text.xview)
    scroll_v.config(command=text.yview)



#jacobiFiles()

b1_3 = font.Font(family='Times New Roman', size=30, weight='bold')

b1 = tk.Button(win, text="Afisare", bg='#e35d34', fg='#000000', borderwidth=4, relief='raised',  height=9, width=15, command=win_ex)
b1['font'] = b1_3
b1.place(relx=0.5, rely=0.5, anchor=CENTER)


win.mainloop()

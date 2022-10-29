from tkinter import font
import tk
from tkinter import *
import tkinter as tk

from main import *


win = tk.Tk()
win.geometry("950x550")
win.title('Exercises')
win.resizable(False, False)


def win_ex1():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("600x100")
    newWindow.title('Precizia')
    newWindow.resizable(False, False)

    txt = Label(newWindow, text='Precizia calculatorului este : ' + str(res[0]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.25)


def win_ex2():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("900x300")
    newWindow.title('Verificarea solutiilor')
    newWindow.resizable(False, False)

    txt = Label(newWindow, text='Verificarea solutiilor :', bg='#f0f0f0', font=('Times New Roman', 30, 'underline'))
    txt.place(relx=0.025, rely=0.025)

    txt = Label(newWindow, text='Solutia 1 (non-bibl) : ' + str(np.linalg.norm(res[1])), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.25)
    txt = Label(newWindow, text='Solutia 2 (bibl) - forma 1 : ' + str(res[2]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.5)
    txt = Label(newWindow, text='Solutia 3 (bibl) - forma 2 : ' + str(res[3]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.75)


def win_ex3():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("1000x650")
    newWindow.title('Verificarea solutiilor')
    newWindow.resizable(False, False)

    txt = Label(newWindow, text='Inversarile matriciilor :', bg='#f0f0f0', font=('Times New Roman', 30, 'underline'))
    txt.place(relx=0.025, rely=0.025)

    txt = Label(newWindow, text='Aproximarea inversii matricei : ' + str(np.linalg.norm(res[5])), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.125)
    txt = Label(newWindow, text='Matricea inversa :  ', bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.25)
    txt = Label(newWindow, text=str(res[4]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.35)


def win_rdm():
    n = 105
    delFs()
    a = genA(n)
    b = genB(n)
    global res
    res = gaussV1(a, b, n)


n = 105
delFs()
a = genA(n)
b = genB(n)
res = gaussV1(a, b, n)


b1_3 = font.Font(family='Times New Roman', size=30, weight='bold')

b1 = tk.Button(win, text="Precizia \n PC-ului", bg='#e35d34', fg='#000000', borderwidth=4, relief='raised', height=6, width=12,
               command=win_ex1)
b1['font'] = b1_3
b1.place(relx=0.175, rely=0.35, anchor=CENTER)
b2 = tk.Button(win, text="Verificarea \n solutiillor", bg='#7bdb63', fg='#000000', borderwidth=4, relief='raised', height=6, width=12,
               command=win_ex2)
b2['font'] = b1_3
b2.place(relx=0.5, rely=0.35, anchor=CENTER)
b3 = tk.Button(win, text="Matricea \n inversata", bg='#6397db', fg='#000000', borderwidth=4, relief='raised', height=6, width=12,
               command=win_ex3)
b3['font'] = b1_3
b3.place(relx=0.825, rely=0.35, anchor=CENTER)
b4 = tk.Button(win, text="Rdm", bg='#ffd257', fg='#000000', borderwidth=4, relief='raised', height=2, width=4,
               command=win_rdm)
b4['font'] = b1_3
b4.place(relx=0.5, rely=0.8, anchor=CENTER)

win.mainloop()

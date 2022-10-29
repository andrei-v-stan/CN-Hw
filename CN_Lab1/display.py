from tkinter import font
import tk
from tkinter import *
import tkinter as tk

from main import *


win = tk.Tk()
win.geometry("1000x700")
win.title('Exercises')
win.resizable(False, False)


def win_ex1():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("600x100")
    newWindow.title('Exercise 1')
    newWindow.resizable(False, False)

    txt = Label(newWindow, text='Precizia calculatorului este : ' + str(ex1()), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.25)


def win_ex2():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("1300x900")
    newWindow.title('Exercise 2')
    newWindow.resizable(False, False)

    u = ex1()

    a = 1.0
    b = u / 10
    c = u / 10

    rez = ex2(u, a, b, c)

    txt = Label(newWindow, text='Verificarea asociativitatii folosid precizia calculatorului (u) : ', bg='#f0f0f0',
                font=('Times New Roman', 30, 'underline'))
    txt.place(relx=0.025, rely=0.025)

    if rez[0] == 0:
        txt = Label(newWindow, text='- Se vede faptul ca operatia nu este asociativa :  ' + str(
            (rez[1] + rez[2]) + rez[3]) + '  &  ' + str(rez[1] + (rez[2] + rez[3])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.1)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[1]) + '   b = ' + str(rez[2]) + '   c = ' + str(rez[3]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.15)
    elif rez[0] == 1:
        txt = Label(newWindow, text='- Se vede faptul ca operatia este asociativa :  ' + str(
            (rez[1] + rez[2]) + rez[3]) + '  &  ' + str(rez[1] + (rez[2] + rez[3])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.1)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[1]) + '   b = ' + str(rez[2]) + '   c = ' + str(rez[3]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.15)

    if rez[4] == 0:
        txt = Label(newWindow, text='- Se vede faptul ca operatia nu este asociativa :  ' + str(
            (rez[5] * rez[6]) * rez[7]) + '  &  ' + str(rez[5] * (rez[6] * rez[7])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.25)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[5]) + '   b = ' + str(rez[6]) + '   c = ' + str(rez[7]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.3)
    elif rez[4] == 1:
        txt = Label(newWindow, text='- Se vede faptul ca operatia este asociativa :  ' + str(
            (rez[5] * rez[6]) * rez[7]) + '  &  ' + str(rez[5] * (rez[6] * rez[7])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.25)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[5]) + '   b = ' + str(rez[6]) + '   c = ' + str(rez[7]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.3)

    if rez[8] == 0:
        txt = Label(newWindow, text='- Se vede faptul ca operatia nu este asociativa :  ' + str(
            (rez[9] * rez[10]) * rez[11]) + '  &  ' + str(rez[9] * (rez[10] * rez[11])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.4)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[9]) + '   b = ' + str(rez[10]) + '   c = ' + str(rez[11]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.45)
    elif rez[8] == 1:
        txt = Label(newWindow, text='- Se vede faptul ca operatia este asociativa :  ' + str(
            (rez[9] * rez[10]) * rez[11]) + '  &  ' + str(rez[9] * (rez[10] * rez[11])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.4)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[9]) + '   b = ' + str(rez[10]) + '   c = ' + str(rez[11]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.45)

    a = random()
    b = random()
    c = random()

    rez = ex2(u, a, b, c)

    txt = Label(newWindow, text='Verificarea asociativitatii folosid numere random : ', bg='#f0f0f0',
                font=('Times New Roman', 30, 'underline'))
    txt.place(relx=0.025, rely=0.525)

    if rez[0] == 0:
        txt = Label(newWindow, text='- Se vede faptul ca operatia nu este asociativa :  ' + str(
            (rez[1] + rez[2]) + rez[3]) + '  &  ' + str(rez[1] + (rez[2] + rez[3])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.6)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[1]) + '   b = ' + str(rez[2]) + '   c = ' + str(rez[3]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.65)
    elif rez[0] == 1:
        txt = Label(newWindow, text='- Se vede faptul ca operatia este asociativa :  ' + str(
            (rez[1] + rez[2]) + rez[3]) + '  &  ' + str(rez[1] + (rez[2] + rez[3])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.6)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[1]) + '   b = ' + str(rez[2]) + '   c = ' + str(rez[3]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.65)

    if rez[4] == 0:
        txt = Label(newWindow, text='- Se vede faptul ca operatia nu este asociativa :  ' + str(
            (rez[5] * rez[6]) * rez[7]) + '  &  ' + str(rez[5] * (rez[6] * rez[7])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.75)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[5]) + '   b = ' + str(rez[6]) + '   c = ' + str(rez[7]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.8)
    elif rez[4] == 1:
        txt = Label(newWindow, text='- Se vede faptul ca operatia este asociativa :  ' + str(
            (rez[5] * rez[6]) * rez[7]) + '  &  ' + str(rez[5] * (rez[6] * rez[7])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.75)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[5]) + '   b = ' + str(rez[6]) + '   c = ' + str(rez[7]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.8)

    if rez[8] == 0:
        txt = Label(newWindow, text='- Se vede faptul ca operatia nu este asociativa :  ' + str(
            (rez[9] * rez[10]) * rez[11]) + '  &  ' + str(rez[9] * (rez[10] * rez[11])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.9)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[9]) + '   b = ' + str(rez[10]) + '   c = ' + str(rez[11]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.95)
    elif rez[8] == 1:
        txt = Label(newWindow, text='- Se vede faptul ca operatia este asociativa :  ' + str(
            (rez[9] * rez[10]) * rez[11]) + '  &  ' + str(rez[9] * (rez[10] * rez[11])), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.9)
        txt = Label(newWindow, text='Pentru :  a = ' + str(
            rez[9]) + '   b = ' + str(rez[10]) + '   c = ' + str(rez[11]), bg='#f0f0f0',
                    font=('Times New Roman', 20, 'bold'))
        txt.place(relx=0.05, rely=0.95)


def win_ex3():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("600x500")
    newWindow.title('Exercise 3')
    newWindow.resizable(False, False)

    res = ex3()
    resDif = [0, 0, 0]
    resDif[0] = res[0] - res[1]
    resDif[1] = res[2] - res[3]
    resDif[2] = res[4] - res[5]

    for i in range(0, 3):
        if resDif[i] < 0:
            resDif[i] = -resDif[i]

    txt = Label(newWindow, text='Aproximari : ', bg='#f0f0f0', font=('Times New Roman', 30, 'underline'))
    txt.place(relx=0.025, rely=0.025)

    txt = Label(newWindow, text='Sin : ' + str(res[0]), bg='#f0f0f0', font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.15)
    txt = Label(newWindow, text='Aproximare sin : ' + str(res[1]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.225)
    txt = Label(newWindow, text='Aproximare sin : ' + str(resDif[0]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.30)

    txt = Label(newWindow, text='Cos : ' + str(res[2]), bg='#f0f0f0', font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.45)
    txt = Label(newWindow, text='Aproximare cos : ' + str(res[3]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.525)
    txt = Label(newWindow, text='Aproximare cos : ' + str(resDif[1]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.60)

    txt = Label(newWindow, text='Ln : ' + str(res[4]), bg='#f0f0f0', font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.75)
    txt = Label(newWindow, text='Aproximare ln : ' + str(res[5]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.825)
    txt = Label(newWindow, text='Aproximare ln : ' + str(resDif[2]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.90)


def win_bonus():
    newWindow = tk.Toplevel(win)
    newWindow.geometry("600x500")
    newWindow.title('Bonus ex')
    newWindow.resizable(False, False)

    res = bonus()
    resDif = [0,0,0]
    resDif[0] = res[0] - res[1]
    resDif[1] = res[2] - res[3]
    resDif[2] = res[4] - res[5]

    for i in range(0,3):
        if resDif[i] < 0:
            resDif[i] = -resDif[i]

    txt = Label(newWindow, text='Aproximari : ', bg='#f0f0f0', font=('Times New Roman', 30, 'underline'))
    txt.place(relx=0.025, rely=0.025)

    txt = Label(newWindow, text='Sin : ' + str(res[0]), bg='#f0f0f0', font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.15)
    txt = Label(newWindow, text='Aproximare sin : ' + str(res[1]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.225)
    txt = Label(newWindow, text='Aproximare sin : ' + str(resDif[0]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.30)

    txt = Label(newWindow, text='Cos : ' + str(res[2]), bg='#f0f0f0', font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.45)
    txt = Label(newWindow, text='Aproximare cos : ' + str(res[3]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.525)
    txt = Label(newWindow, text='Aproximare cos : ' + str(resDif[1]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.60)

    txt = Label(newWindow, text='Ln : ' + str(res[4]), bg='#f0f0f0', font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.75)
    txt = Label(newWindow, text='Aproximare ln : ' + str(res[5]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.825)
    txt = Label(newWindow, text='Aproximare ln : ' + str(resDif[2]), bg='#f0f0f0',
                font=('Times New Roman', 20, 'bold'))
    txt.place(relx=0.1, rely=0.90)


b1_3 = font.Font(family='Times New Roman', size=30, weight='bold')

b1 = tk.Button(win, text="Exercise 1", bg='#e35d34', fg='#000000', borderwidth=4, relief='raised',  height=6, width=12, command=win_ex1)
b1['font'] = b1_3
b1.place(relx=0.175, rely=0.25, anchor=CENTER)
b2 = tk.Button(win, text="Exercise 2", bg='#7bdb63', fg='#000000', borderwidth=4, relief='raised',  height=6, width=12, command=win_ex2)
b2['font'] = b1_3
b2.place(relx=0.5, rely=0.25, anchor=CENTER)
b3 = tk.Button(win, text="Exercise 3", bg='#6397db', fg='#000000', borderwidth=4, relief='raised',  height=6, width=12, command=win_ex3)
b3['font'] = b1_3
b3.place(relx=0.825, rely=0.25, anchor=CENTER)
b4 = tk.Button(win, text="Bonus Ex", bg='#ffd257', fg='#000000', borderwidth=4, relief='raised', height=6, width=12,
               command=win_bonus)
b4['font'] = b1_3
b4.place(relx=0.5, rely=0.75, anchor=CENTER)

win.mainloop()

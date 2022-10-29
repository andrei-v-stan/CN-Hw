import random as randm

import numpy as np


def delFs():  # delete content in files a.txt and b.txt
    open('a.txt', 'w').close()
    open('b.txt', 'w').close()


def genA(n):  # generate matrix a
    with open('a.txt', 'a') as f:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                x = randm.uniform(-20.0, 20.0)
                f.write(str(x))
                f.write(' ')
            f.write('\n')
    a = np.loadtxt("a.txt")
    return a


def genB(n):  # generate vector b
    with open('b.txt', 'a') as f:
        for i in range(1, n + 1):
            x = randm.uniform(-20.0, 20.0)
            f.write(str(x))
            f.write('\n')
    b = np.loadtxt("b.txt")
    return b


def mod(x):  # modulul unui numar
    if x < 0:
        x = -x
    return x


def pivotP(a, l, n):  # cauta pivot() - pivotare partiala
    maxAio = l
    maxAiol = a[maxAio][maxAio]

    for i in range(l, n):
        temp = a[i][l]
        temp = mod(temp)
        if temp > maxAiol:
            maxAiol = temp
            maxAio = i

    return maxAio


def interLinii(a, b, l, cp, n):  # interschimba linii()
    for i in range(0, n):
        temp = a[l][i]
        temp2 = a[cp][i]
        a[l][i] = temp2
        a[cp][i] = temp
    b[[l, cp]] = b[[cp, l]]


def rsst(A, b, n):
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += A[i][j] * x[j]
        x[i] = (b[i] - sum) / A[i][i]
    return x


def vfsol(Xgauss):  # verifica_solutie()
    a = np.loadtxt("a.txt")
    b = np.loadtxt("b.txt")

    rez = np.dot(a, Xgauss) - b

    return rez


def vfsolb(x_gauss):
    a = np.loadtxt("a.txt")
    b = np.loadtxt("b.txt")

    x1 = np.linalg.solve(a, b)
    x2 = np.linalg.inv(a).dot(b)

    rez = [np.linalg.norm(x_gauss - x1), np.linalg.norm(x_gauss - x2)]

    return rez


def gaussV(a, b, ep, n, m):
    l = 1
    cp = pivotP(a, l - 1, n)
    if l != cp:
        interLinii(a, b, l - 1, cp, n)

    while l < n and mod(a[l - 1][l - 1]) > ep:
        for li in range(l, n):
            f = a[li][l - 1] / a[l - 1][l - 1]
            for lj in range(l, m):
                a[li][lj] = a[li][lj] - f * a[l - 1][lj]
            b[li] = b[li] - f * b[l - 1]
            a[li][l - 1] = 0
        l = l + 1
        cp = pivotP(a, l - 1, n)
        interLinii(a, b, l - 1, cp, n)

    if mod(a[l - 1][l - 1]) <= ep:
        print('matrice singulara')

    else:
        Xgauss = rsst(a, b, n)
        # vfsol(Xgauss)
        # vfsolb(Xgauss)

    return Xgauss


def ci(a, n, ep):        # calcularea inversei matricii
    a = np.loadtxt("a.txt")
    b = np.loadtxt("b.txt")

    idm = np.identity(n)
    # A = gaussV(a, b, ep, n, 2 * n)

    return a


def cib(a, n, ep):       # solutionarea inversei folosing gauss si biblioteca
    inva = np.linalg.inv(a)
    sola = ci(a, n, ep)
    res = inva - sola

    return res

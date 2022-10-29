from func import *


def eps():  # precizia masinii
    u = 10
    m = -1

    while 1.0 + u != 1.0:
        m = m + 1
        u = u / 10

    pm = pow(10, -m + 1)
    return pm


def gaussV1(a, b, n):
    ep = eps()
    print(ep)
    l = 1
    cp = pivotP(a, l - 1, n)
    if l != cp:
        interLinii(a, b, l - 1, cp, n)

    while l < n and mod(a[l - 1][l - 1]) > ep:
        for li in range(l, n):
            f = a[li][l - 1] / a[l - 1][l - 1]
            for lj in range(l, n):
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
        rezvf = vfsol(Xgauss)
        rezvfb = vfsolb(Xgauss)
        rezci = ci(a, n, ep)
        rezcib = cib(a, n, ep)
        print("Rezultatul verificarii solutiei : ", np.linalg.norm(rezvf))
        print("Rezultatul verificarii solutiei b : ", "\n\tForma 1 norm : ", rezvfb[0], "\n\tForma 2 norm : ",
              rezvfb[1])
        print("Rezultatul invers a matricei este : \n", rezci)
        print("Rezultatul aproximarii inverse a matricei este : ", np.linalg.norm(rezcib))
        print('\n')

    res = [ep, rezvf, rezvfb[0], rezvfb[1], rezci, rezcib]

    return res


if __name__ == '__main__':
    n = int(input("WHat is the size of the matrix : "))
    delFs()
    a = genA(n)
    b = genB(n)

    gaussV1(a, b, n)

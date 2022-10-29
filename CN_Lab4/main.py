import filecmp

a1 = open("files/a_1.txt", "r")
A1 = {(-1, -1): -1}
b1 = open("files/b_1.txt", "r")
B1 = {}
a2 = open("files/a_2.txt", "r")
A2 = {}
b2 = open("files/b_2.txt", "r")
B2 = {}
a3 = open("files/a_3.txt", "r")
A3 = {}
b3 = open("files/b_3.txt", "r")
B3 = {}
a4 = open("files/a_4.txt", "r")
A4 = {}
b4 = open("files/b_4.txt", "r")
B4 = {}
a5 = open("files/a_5.txt", "r")
A5 = {}
b5 = open("files/b_5.txt", "r")
B5 = {}

mya1 = open("files/myA1.txt", "w")
mya2 = open("files/myA2.txt", "w")
mya3 = open("files/myA3.txt", "w")
mya4 = open("files/myA4.txt", "w")
mya5 = open("files/myA5.txt", "w")

myb1 = open("files/myB1.txt", "w")
myb2 = open("files/myB2.txt", "w")
myb3 = open("files/myB3.txt", "w")
myb4 = open("files/myB4.txt", "w")
myb5 = open("files/myB5.txt", "w")

X_c = []
X_p = []


def Readfile(file, output):
    output[-1, -1] = int(file.readline())
    file.readline()
    Lines = file.readlines()

    for line in Lines:
        element = line.replace('\n', "").split(" , ")
        output[int(element[1]), int(element[2])] = float(element[0])


def CheckDiag(matrice):
    check = True

    for i in range(0, int(matrice[-1, -1])):
        if (i, i) in matrice:
            if matrice[i, i] == 0:
                check = False
        else:
            print("nu exista element pe pozitia :=", i)

    return check


def ReadB(file, output):
    Lines = file.readlines()
    count = 0

    for line in Lines:
        element = line.replace('\n', "").split(" , ")
        output[count] = float(element[0])
        count += 1


def WriteB(lista, output):
    for i in range(0, len(lista)):
        myString = str(lista[i]).replace(".0", "") + "\n"
        output.write(myString)


def WriteA(matrice, output):
    output.write(str(matrice[-1, -1]))
    output.write("\n")
    output.write("\n")

    for x in matrice:
        if x != (-1, -1):
            myString = str(matrice[x]).replace(".0", "") + " , " + str(x[0]) + " , " + str(x[1]) + "\n"
            output.write(myString)


def compareAll():
    file1 = ["files/a_1.txt", "files/a_2.txt", "files/a_3.txt", "files/a_4.txt", "files/a_5.txt", ]
    file2 = ["files/myA1.txt", "files/myA2.txt", "files/myA3.txt", "files/myA4.txt", "files/myA5.txt", ]

    ct = 0
    printM = []

    print('')
    for i in range(0, 5):
        result = filecmp.cmp(file1[i], file2[i])

        if result == 0:
            printM.append("Check A" + str(i + 1) + ": success")
            print(printM[ct])
            ct += 1

    file1 = ["files/b_1.txt",
             "files/b_2.txt",
             "files/b_3.txt",
             "files/b_4.txt",
             "files/b_5.txt", ]

    file2 = ["files/myB1.txt",
             "files/myB2.txt",
             "files/myB3.txt",
             "files/myB4.txt",
             "files/myB5.txt", ]

    print('')
    for i in range(0, 5):
        result = filecmp.cmp(file1[i], file2[i])

        if result == 0:
            printM.append("Check B" + str(i + 1) + ": success")
            print(printM[ct])
            ct += 1

    return printM


def epsilon(k):
    return pow(10, -k)


def delta(A, B, X):
    d = []
    for i in range(0, A[-1, -1]):
        val = 0
        for j in range(0, A[-1, -1]):
            if (j, i) in A:
                val += A[j, i] * X[j] - B[j]
        d.append(val)

    return d


def jacobi(Ax, Bx):
    X_cX = []
    X_pX = []

    printP = []

    for i in range(0, Ax[-1, -1]):
        X_cX.append(0)
        X_pX.append(0)

    impartitor = 0
    k = 1
    found = False

    while found == False:

        printP.append('\n\nSe face iteratia : ' + str(k) + '\n\n')
        print('\n\nSe face iteratia :', k, '\n\n')
        foundVal = True

        for i in range(0, len(X_pX)):
            X_cX[i] = X_pX[i]

        for i in range(0, Ax[-1, -1]):
            if i % 100 == 0:
                print(i)
            impartitor = 0
            newValue = Bx[i]

            for j in range(0, Ax[-1, -1]):
                if i == j:
                    impartitor = Ax[i, j]
                else:
                    if (i, j) in Ax:
                        newValue -= Ax[i, j] * X_cX[j]
                    elif i > j and (j, i) in Ax:
                        newValue -= Ax[j, i] * X_cX[j]

            X_pX[i] = newValue / impartitor
        d = delta(Ax, Bx, X_pX)
        for i in range(0, len(X_pX)):

            if k <= 1 and abs(X_pX[i] - X_cX[i]) > epsilon(k):
                printP.append(" Pentru pozitia " + str(i) + " delta este " + str(d[i]) + " iar diferenta este " + str(
                    abs(X_pX[i] - X_cX[i])) + " care este mai mare fata de epsilonul " + str(
                    epsilon(k)) + " si valorile " + str(X_pX[i]) + " & " + str(X_cX[i]))
                print(" Pentru pozitia ", i, " delta este ", d[i], " iar diferenta este ", abs(X_pX[i] - X_cX[i]),
                      " care este mai mare fata de epsilonul ",
                      epsilon(k), " si valorile ", X_pX[i], X_cX[i])
                foundVal = False

        if foundVal == True or k == 1:
            found = True
        else:
            k += 1

    return printP


def mainD():
    printP = []

    for i in range(0, A2[-1, -1]):
        X_c.append(0)
        X_p.append(0)

    impartitor = 0
    k = 1
    found = False

    while found == False:

        printP.append('\n\nSe face iteratia : ' + str(k) + '\n\n')
        print('\n\nSe face iteratia :', k, '\n\n')
        foundVal = True

        for i in range(0, len(X_p)):
            X_c[i] = X_p[i]

        for i in range(0, A2[-1, -1]):
            impartitor = 0
            newValue = B2[i]

            for j in range(0, A2[-1, -1]):
                if i == j:
                    impartitor = A2[i, j]
                else:
                    if (i, j) in A2:
                        newValue -= A2[i, j] * X_c[j]
                    elif i > j and (j, i) in A2:
                        newValue -= A2[j, i] * X_c[j]

            X_p[i] = newValue / impartitor

        for i in range(0, len(X_p)):

            if k <= 8 and abs(X_p[i] - X_c[i]) > epsilon(k):
                printP.append(" Pentru pozitia " + str(i) + " diferenta este " + str(
                    abs(X_p[i] - X_c[i])) + " care este mai mare fata de epsilonul " + str(
                    epsilon(k)) + " si valorile " + str(X_p[i]) + " & " + str(X_c[i]))
                print(" Pentru pozitia ", i, " diferenta este ", abs(X_p[i] - X_c[i]),
                      " care este mai mare fata de epsilonul ",
                      epsilon(k), " si valorile ", X_p[i], X_c[i])
                foundVal = False

        if foundVal == True or k == 8:
            found = True
        else:
            k += 1

    return printP


def jacobiFiles():
    Readfile(a1, A1)
    Readfile(a2, A2)
    Readfile(a3, A3)
    Readfile(a4, A4)
    Readfile(a5, A5)

    print('\n')
    print("Check A1:", CheckDiag(A1))
    print("Check A2:", CheckDiag(A2))
    print("Check A3:", CheckDiag(A3))
    print("Check A4:", CheckDiag(A4))
    print("Check A5:", CheckDiag(A5))

    ReadB(b1, B1)
    ReadB(b2, B2)
    ReadB(b3, B3)
    ReadB(b4, B4)
    ReadB(b5, B5)

    WriteA(A1, mya1)
    WriteA(A2, mya2)
    WriteA(A3, mya3)
    WriteA(A4, mya4)
    WriteA(A5, mya5)

    WriteB(B1, myb1)
    WriteB(B2, myb2)
    WriteB(B3, myb3)
    WriteB(B4, myb4)
    WriteB(B5, myb5)

    compareAll()

    myx2 = open('files/x2.txt', 'w')

    checks = compareAll()
    myx2.write('\n')

    for wr in checks:
        myx2.write(wr)
        myx2.write('\n')

    prints = jacobi(A2, B2)
    myx2.write('\n\n')

    for wr in prints:
        myx2.write(wr)
        myx2.write('\n')

    myx2.close()

    myx1 = open('files/x1.txt', 'w')

    checks = compareAll()
    myx1.write('\n')

    for wr in checks:
        myx1.write(wr)
        myx1.write('\n')

    prints = jacobi(A1, B1)
    myx1.write('\n\n')

    for wr in prints:
        myx1.write(wr)
        myx1.write('\n')

    myx1.close()

    myx3 = open('files/x3.txt', 'w')

    checks = compareAll()
    myx3.write('\n')

    for wr in checks:
        myx3.write(wr)
        myx3.write('\n')

    prints = jacobi(A3, B3)
    myx3.write('\n\n')

    for wr in prints:
        myx3.write(wr)
        myx3.write('\n')

    myx3.close()

    myx4 = open('files/x4.txt', 'w')

    checks = compareAll()
    myx4.write('\n')

    for wr in checks:
        myx4.write(wr)
        myx4.write('\n')

    prints = jacobi(A4, B4)
    myx4.write('\n\n')

    for wr in prints:
        myx4.write(wr)
        myx4.write('\n')

    myx4.close()

    myx5 = open('files/x5.txt', 'w')

    checks = compareAll()
    myx5.write('\n')

    for wr in checks:
        myx5.write(wr)
        myx5.write('\n')

    prints = jacobi(A5, B5)
    myx5.write('\n\n')

    for wr in prints:
        myx5.write(wr)
        myx5.write('\n')

    myx5.close()


if __name__ == "__main__":
    jacobiFiles()

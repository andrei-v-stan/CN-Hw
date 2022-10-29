
myA = open("files/myA.txt", "w")
myB = open("files/myB.txt", "w")


T = [0,0]
A = [        [     ],[     ]      ]
B = [        [     ],[     ]      ]
Sum = [             ]
Prod = [             ]


def display():
    elemNrA = readA()
    readB(elemNrA)
    mulAA()
    addAB()



def readA():
    a = open("files/a.txt", "r")
    elementsNrA = a.readline()
    a.readline()
    for i in range(0,int(elementsNrA)):
        txt = a.readline()
        myTXT = txt.replace('\n',"").split(",")
        while int(myTXT[1]) > len(A) - 1:
            A.append([])
        X = [float(myTXT[0]) ,int(myTXT[2])]
        A[int(myTXT[1])].append(X)

    print("S-a realizat citirea lui A")
    for i in range(0,len(A)):
        myA.write(str(A[i]))
        myA.write("\n")
    a.close()
    myA.close()

    return elementsNrA



def readB(elementsNrA):
    b = open("files/b.txt", "r")
    elementsNrB = b.readline()
    b.readline()
    for i in range(0,int(elementsNrA)):
        txt = b.readline()
        myTXT = txt.replace('\n',"").split(",")
        while int(myTXT[1]) > len(B) - 1:
            B.append([])
        X = [float(myTXT[0]) ,int(myTXT[2])]
        B[int(myTXT[1])].append(X)

    print("S-a realizat citirea lui B")
    for i in range(0,len(B)):
        myB.write(str(B[i]))
        myB.write("\n")
    b.close()
    myB.close()


def lengthAB():
    while len(A)>len(B):
        B.append([])
    while len(B)>len(A):
        A.append([])



def addAB():
    s = open("files/mySum.txt", "w")
    # ptu fiecare linie se repeta
    for i in range(0,len(A)):
        Sum.append([])
        newrow = A[i]+B[i]
        # ptu fiecare element din newrow
        for j in range(0, len(newrow)):
            jInSum = False
            if len(newrow)>0:
                # fac check daca nu cumva pe pozitia j deja este cv
                for k in range(0,len(Sum[i])):
                    if Sum[i][k][1] == newrow[j][1]:
                        Sum[i][k][0] = Sum[i][k][0]+newrow[j][0]
                        jInSum=True
                # daca nu este nimic ii dau append doar
                if not jInSum:
                    Sum[i].append(newrow[j])
    for i in range(0,len(Sum)):
        s.write(str(Sum[i]))
        s.write("\n")
    print("S-a realizat suma A+B")
    s.close()



def getMultiplied(rand,pozitie):

    print(A[rand])
    value = 0
    for valoarea1_cautata in range(0,len(A[rand])):
        rand_Nou = A[rand][valoarea1_cautata][1]
        for i in range(0,len(A[rand_Nou])):
            if A[rand_Nou][i][1]==A[rand][valoarea1_cautata][1]:
                print(" inmultesc acuma" ,A[rand][valoarea1_cautata], "cu ", A[rand_Nou][i])
                value = value + A[rand][valoarea1_cautata][0]*A[rand_Nou][i][0]
                print("pe pozitia", rand,pozitie,"avem" , value)
                newVal =[value, pozitie]
    Prod[rand].append(newVal)



def mulAA():
    p = open("Files/myProd.txt", "w")
    value = 0
    newRow = []

    for randul_curent in range(0, len(A)):
        Prod.append([])
        if len(A[randul_curent]) > 0:
            for pozitia_curenta in range(0, len(A[randul_curent])):
                getMultiplied(randul_curent, pozitia_curenta)

    for i in range(0, len(Prod)):
        p.write(str(Prod[i]))
        p.write("\n")
    p.close()



if __name__ == "__main__":
    display()

from random import random
import random as randm
import math
from numpy import sqrt


sin_a = [1805490264.690988571178600370234394843221, -164384678.227499837726129612587952660511,
         3664210.647581261810227924465160827365, -28904.140246461781357223741935980097,
         76.568981088717405810132543523682]
sin_b = [2298821602.638922662086487520330827251172, 27037050.118894436776624866648235591988,
         155791.388546947693206469423979505671, 540.567501261284024767779280700089, 1.0]
cos_a = [1090157078.174871420428849017262549038606, -321324810.993150712401352959397648541681,
         12787876.849523878944051885325593878177, -150026.206045948110568310887166405972,
         538.333564203182661664319151379451]
cos_b = [1090157078.174871420428867295670039506886, 14907035.776643879767410969509628406502,
         101855.811943661368302608146695082218, 429.772865107391823245671264489311, 1.0]
ln_a = [75.151856149910794642732375452928, -134.730399688659339844586721162914, 74.201101420634257326499008275515,
        -12.777143401490740103758406454323, 0.332579601824389206151063529971]
ln_b = [37.575928074955397321366156007781, -79.890509202648135695909995521310, 56.215534829542094277143417404711,
        -14.516971195056682948719125661717, 1.0]


def ex1():
    u = 10
    m = -1

    while 1.0 + u != 1.0:
        m = m + 1
        u = u / 10

    pm = pow(10, -m + 1)
    return pm


def ex2(u,a,b,c):
    rez = []

    if (a + b) + c != a + (b + c):
        rez0 = 0
    else:
        rez0 = 1
    rez.extend([rez0, a, b, c])

    if (a * b) * c != a * (b * c):
        rez1 = 0
    else:
        rez1 = 1
    rez.extend([rez1, a, b, c])

    while (a * b) * c == a * (b * c):
        a = a / 10

    if (a * b) * c != a * (b * c):
        rez2 = 0
    else:
        rez2 = 1

    rez.extend([rez2, a, b, c])

    return rez


def relationsP(y, a):
    return a[0] + y * (a[1] + y * (a[2] + y * (a[3] + y * a[4])))


def relationsQ(y, b):
    return b[0] + y * (b[1] + y * (b[2] + y * (b[3] + y * b[4])))


def ex3():
    res = []

    x = randm.uniform(-1.0, 1.0)
    sin1 = math.sin((1 / 4) * math.pi * x)
    sin2 = x * relationsP(x * x, sin_a) / relationsQ(x * x, sin_b)

    x = randm.uniform(-1.0, 1.0)
    cos1 = math.cos((1 / 4) * math.pi * x)
    cos2 = relationsP(x * x, cos_a) / relationsQ(x * x, cos_b)

    x = randm.uniform(1 / sqrt(2), sqrt(2))
    z = (x - 1) / (x + 1)
    ln1 = math.log(x)
    ln2 = z * relationsP(z * z, ln_a) / relationsQ(z * z, ln_b)

    res.extend([sin1, sin2, cos1, cos2, ln1, ln2])

    return res


def bonus():
    rez = []

    x = randm.random()
    while (x <= -1):
        x += 8
    while (x >= 8):
        x -= 8

    if (x >= 2 and x < 4):      # cadran2
        x = math.pi - x
        sin1 = math.sin((1 / 4) * math.pi * x)
    elif (x >= 4 and x < 6):    # cadran3
        x = math.pi + x
        if x >= 8:
            x -= 8
        sin1 = -(math.sin((1 / 4) * math.pi * x))
    elif (x >= 6 and x < 7):    # cadran4 < -pi/4
        x = 2 * math.pi - x
        sin1 = -(math.sin((1 / 4) * math.pi * x))
    elif (x > 1 and x < 2):     # cadran 1 > pi/4
        x = math.pi + x
        sin1 = -(math.sin((1 / 4) * math.pi * x))
    else: # (x <= 1 | | x > -1)
        sin1 = math.sin((1 / 4) * math.pi * x)

    sin2 = x * relationsP(x * x, sin_a) / relationsQ(x * x, sin_b)

    x = randm.random()
    while (x <= -1):
        x += 8
    while (x >= 8):
        x -= 8

    if (x >= 2 and x < 4):      # cadran2
        x = math.pi - x
        cos1 = -(math.cos((1 / 4) * math.pi * x))
    elif (x >= 4 and x < 6):    # cadran3
        x = math.pi + x
        if (x >= 8):
            x -= 8
        cos1 = -(math.cos((1 / 4) * math.pi * x))
    elif (x >= 6 and x < 7):    # cadran4 < -pi/4
        x = 2 * math.pi - x
        cos1 = math.cos((1 / 4) * math.pi * x)
    elif (x > 1 and x < 2):     # cadran 1 > pi/4
        x = math.pi + x
        cos1 = math.cos((1 / 4) * math.pi * x)
    else: # (x <= 1 | | x > -1)
        cos1 = math.cos((1 / 4) * math.pi * x)

    cos2 = relationsP(x * x, cos_a) / relationsQ(x * x, cos_b)

    x = randm.uniform(1 / sqrt(2), sqrt(2))
    z = (x - 1) / (x + 1)
    ln1 = math.log(x) / math.log(2.71828)
    ln2 = z * relationsP(z * z, ln_a) / relationsQ(z * z, ln_b)

    rez.extend([sin1, sin2, cos1, cos2, ln1, ln2])

    return rez

if __name__ == '__main__':

    u = ex1()
    print("\nEx 1:")
    print("Precizia masinii este :", u, "\n")



    print("\n\nEx 2:")

    a = 1.0
    b = u / 10
    c = u / 10

    rez = ex2(u, a, b, c)

    if rez[0] == 0:
        print("Se vede faptul ca operatia nu este asociativa :", (rez[1] + rez[2]) + rez[3], "&",
              rez[1] + (rez[2] + rez[3]), "\nPentru :", "a =", rez[1], "  b =", rez[2], "  c =", rez[3], "\n")
    elif rez[0] == 1:
        print("Se vede faptul ca operatia este asociativa :", (rez[1] + rez[2]) + rez[3], "&",
              rez[1] + (rez[2] + rez[3]), "\nPentru :", "a =", rez[1], "  b =", rez[2], "  c =", rez[3], "\n")

    if rez[4] == 0:
        print("Se vede faptul ca operatia nu este asociativa :", (rez[5] * rez[6]) * rez[7], "&",
              rez[5] * (rez[6] * rez[7]), "\nPentru :", "a =", rez[5], "  b =", rez[6], "  c =", rez[7], "\n")
    elif rez[4] == 1:
        print("Se vede faptul ca operatia este asociativa :", (rez[5] * rez[6]) * rez[7], "&",
              rez[5] * (rez[6] * rez[7]), "\nPentru :", "a =", rez[5], "  b =", rez[6], "  c =", rez[7], "\n")

    if rez[8] == 0:
        print("Se vede faptul ca operatia nu este asociativa :", (rez[9] * rez[10]) * rez[11], "&",
              rez[9] * (rez[10] * rez[11]), "\nPentru :", "a =", rez[9], "  b =", rez[10], "  c =", rez[11], "\n")
    elif rez[8] == 1:
        print("Se vede faptul ca operatia este asociativa :", (rez[9] * rez[10]) * rez[11], "&",
              rez[9] * (rez[10] * rez[11]), "\nPentru :", "a =", rez[9], "  b =", rez[10], "  c =", rez[11], "\n")



    print("\n\nEx 2 - Random:")

    a = random()
    b = random()
    c = random()

    rez = ex2(u, a, b, c)

    if rez[0] == 0:
        print("Se vede faptul ca operatia nu este asociativa :", (rez[1] + rez[2]) + rez[3], "&",
              rez[1] + (rez[2] + rez[3]), "\nPentru :", "a =", rez[1], "  b =", rez[2], "  c =", rez[3], "\n")
    elif rez[0] == 1:
        print("Se vede faptul ca operatia este asociativa :", (rez[1] + rez[2]) + rez[3], "&",
              rez[1] + (rez[2] + rez[3]), "\nPentru :", "a =", rez[1], "  b =", rez[2], "  c =", rez[3], "\n")

    if rez[4] == 0:
        print("Se vede faptul ca operatia nu este asociativa :", (rez[5] * rez[6]) * rez[7], "&",
              rez[5] * (rez[6] * rez[7]), "\nPentru :", "a =", rez[5], "  b =", rez[6], "  c =", rez[7], "\n")
    elif rez[4] == 1:
        print("Se vede faptul ca operatia este asociativa :", (rez[5] * rez[6]) * rez[7], "&",
              rez[5] * (rez[6] * rez[7]), "\nPentru :", "a =", rez[5], "  b =", rez[6], "  c =", rez[7], "\n")

    if rez[8] == 0:
        print("Se vede faptul ca operatia nu este asociativa :", (rez[9] * rez[10]) * rez[11], "&",
              rez[9] * (rez[10] * rez[11]), "\nPentru :", "a =", rez[9], "  b =", rez[10], "  c =", rez[11], "\n")
    elif rez[8] == 1:
        print("Se vede faptul ca operatia este asociativa :", (rez[9] * rez[10]) * rez[11], "&",
              rez[9] * (rez[10] * rez[11]), "\nPentru :", "a =", rez[9], "  b =", rez[10], "  c =", rez[11], "\n")



    print("\n\nEx 3:")
    res = ex3()
    resDif = [0,0,0]
    resDif[0] = res[0] - res[1]
    resDif[1] = res[2] - res[3]
    resDif[2] = res[4] - res[5]

    for i in range(0,3):
        if resDif[i] < 0:
            resDif[i] = -resDif[i]

    print("\nSin : ", res[0], "\nAproximare sin : ", res[1], "\nDiferenta sin : ", resDif[0], "\n\nCos : ", res[2], "\nAproximare cos : ", res[3], "\nDiferenta cos : ", resDif[1], "\n\nLn : ", res[4], "\nAproximare ln : ", res[5], "\nDiferenta ln : ", resDif[2])


    print("\n\nBonus ex:")
    rez = bonus()
    rezDif = [0,0,0]
    rezDif[0] = rez[0] - rez[1]
    rezDif[1] = rez[2] - rez[3]
    rezDif[2] = rez[4] - rez[5]

    for i in range(0,3):
        if rezDif[i] < 0:
            rezDif[i] = -rezDif[i]

    print("\nSin : ", rez[0], "\nAproximare sin : ", rez[1], "\nDiferenta sin : ", rezDif[0], "\n\nCos : ", rez[2], "\nAproximare cos : ", rez[3], "\nDiferenta cos : ", rezDif[1], "\n\nLn : ", rez[4], "\nAproximare ln : ", rez[5], "\nDiferenta ln : ", rezDif[2])



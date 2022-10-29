
def eps():
    u = 10
    m = -1

    while 1.0 + u != 1.0:
        m = m + 1
        u = u / 10

    pm = pow(10, -m + 1)
    return pm


def horner(a, v):
    b0 = a[0]
    bn = a[1] + b0 * v

    for i in range(2, len(a)):
        bi = a[i] + bn * v
        bn = bi

    return bn


def zeroTest(val, ep):
    if val < 0:
        tempVal = -val
    else:
        tempVal = val

    if ep < 0:
        tempEps = -ep
    else:
        tempEps = ep

    if tempVal < ep and val < 0:
        return tempEps

    elif tempVal < ep:
        return ep

    else:
        return val


def dehghan(a, x0, ep):
    k = 1
    kMax = 10000

    solFile = open('sol.txt', 'w')
    solFile.write('\n')

    while True:

        pK = horner(a, x0)
        pSum = horner(a, x0 + pK)
        pDif = horner(a, x0 - pK)

        if pK < 0:
            tempPk = -pK
        else:
            tempPk = pK

        if tempPk <= ep / 10.0:
            delX = 0.0

        else:
            pSD = pSum - pDif

            pKy = pK * pK
            y = x0 - (2 * pKy) / zeroTest(pSD, ep)

            pKx = pK * (pK + horner(a, y))
            delX = (2 * pKx) / zeroTest(pSD, ep)

        x0 = x0 - delX

        ite = 'Iteratia ' + str(k) + ' : ' + '\tx0 = ' + str(x0) + '\t\tdelta = ' + str(delX)
        solFile.write(ite + '\n')

        k = k + 1

        if delX < 0:
            tempDel = -delX
        else:
            tempDel = delX

        if tempDel < ep or k > kMax or tempDel > 10 ** 8:
            break

    solFile.write('\n\n')
    solFile.close()

    if delX < ep:
        return x0
    else:
        return 'div'


def inteR(a):
    if a[0] < 0:
        tempA = -a[0]
    else:
        tempA = a[0]

    tempMax = max(a, key=abs)

    if tempMax < 0:
        tempMax = -tempMax

    r = (tempA + tempMax) / tempA

    return r


def sol(a, r):
    s = []
    tempR = int(r)

    for i in range(-tempR, tempR + 1):
        x = dehghan(a, i, ep)
        if x != 'div' and x not in s and x - round(x, 2) == 0.0:
            s.append(x)

    return s


if __name__ == '__main__':

    ep = eps()
    print(ep)

    a = [[1.0, -6.0, 11.0, -6.0], [42.0, -55.0, -42.0, 49.0, -6.0], [8.0, -38.0, 49.0, -22.0, 3.0],
         [1.0, -6.0, 13.0, -12.0, 4.0]]

    r = [inteR(a[0]), inteR(a[1]), inteR(a[2]), inteR(a[3])]

    s_p1 = sol(a[0], r[0])
    s_p2 = sol(a[1], r[1])
    s_p3 = sol(a[2], r[2])
    s_p4 = sol(a[3], r[3])

    solFile = open('sol.txt', 'a')

    solFile.write(('The solutions for' + ' P1: ' + str(s_p1) + '\n'))
    solFile.write(('The solutions for' + ' P2: ' + str(s_p2) + '\n'))
    solFile.write(('The solutions for' + ' P3: ' + str(s_p3) + '\n'))
    solFile.write(('The solutions for' + ' P4: ' + str(s_p4) + '\n'))

    solFile.close()

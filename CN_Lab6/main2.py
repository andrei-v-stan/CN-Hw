import math
import numpy as np


def horner(a, x):
    d = a[len(a)-1]

    i = len(a)-2
    while i >= 0:
        d = a[i] + d*x
        i = i-1

    return d


def polynom(x0, xn, n, x, function):
    values = []
    values.append((x0, function(x0)))
    diff = (xn - x0) / n

    for i in range(1, n):
        values.append((x0 + i*diff, function(x0 + i*diff)))

    values.append((xn, function(xn)))

    B = np.array([[values[i][0]**j for j in range(n+1)] for i in range(n+1)])
    f = np.array([values[i][1] for i in range(n+1)])

    a = np.dot(np.linalg.inv(B), f)


    print("Solutie folosind polinoame: ")
    sol = horner(a, x)
    print(sol)

    print("")

    print("Solutie reala: ")
    print(function(x))

    print("")
    print("Eroare: ")
    print(abs(sol - function(x)))



def compute_A(i, values, da):
    if(i == 0):
        return da
    else:
        return -compute_A(i-1, values, da) + (2*(values[i][1] - values[i-1][1])/(values[i][0] - values[i-1][0]))


def spline(x0, xn, n, x, function, derivate):
    da = derivate(x0)

    values = []
    values.append((x0, function(x0)))
    diff = (xn - x0) / n

    for i in range(1, n):
        values.append((x0 + i * diff, function(x0 + i * diff)))

    values.append((xn, function(xn)))

    i = 0
    while x > values[i][0]:
        i = i+1

    sol = ((compute_A(i, values, da) - compute_A(i-1, values, da))/(2*(values[i][0] - values[i-1][0])))*((x - values[i-1][0])**2) + compute_A(i-1, values, da) * (x - values[i-1][0]) + values[i-1][1]

    print("Solutie folosind spline: ")
    print(sol)

    print("")

    print("Solutie reala: ")
    print(function(x))

    print("")
    print("Eroare: ")
    print(abs(sol - function(x)))



if __name__ == '__main__':

    print("Choose a function: ")
    print("\t1: x^2 -12x + 30")
    print("\t2: sin(x) - cos(x)")
    print("\t3: 2x^3 - 3x + 15")

    funCase = int(input())

    n = int(input("n: "))
    x = float(input("x: "))


    match funCase:

        case 1:
            x0 = 1
            xn = 5
            function = x**2 - 12*x + 30
            derivate = 2 * x - 12

        case 2:
            x0 = 0
            xn = 1.5
            function = math.sin(x) - math.cos(x)
            derivate = math.sin(x) + math.cos(x)

        case 3:
            x0 = 0
            xn = 2
            function = 2*(x**3) - 3*x + 15
            derivate = 6 * (x ** 2) - 3


    if not x0 < x < xn:
        exit(0)

    print("\n\n\n\n")
    polynom(x0, xn, n, x, function)

    print("\n\n\n\n")
    spline(x0, xn, n, x, function, derivate)

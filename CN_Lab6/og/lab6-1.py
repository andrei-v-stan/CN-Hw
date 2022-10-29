import numpy


def f(x):
    return x ** 4 + 12 * x ** 3 + 30 * x ** 2 + 12
    # x ** 2 - 12 * x + 30
    # x ** 4 + 12 * x ** 3 + 30 * x ** 2 + 12 = x^4 + 12x^3 + 30x^2 + 12
    # (5, 4, 1(x0), 5(xn), 3)
    # (3, 3, 1, 5, 2) - aka (max degree = max power + 1, nr of operations, x0, xn, nr of operations with x)


def least_squares(n, m, x0, xn, x):
    h = (xn - x0) / n
    points = [(x0, f(x0))]

    for i in range(1, n):
        points.append((x0 + i * h, f(x0 + i * h)))

    points.append((xn, f(xn)))

    a = numpy.array([[sum([point[0] ** (i + j) for point in points]) for j in range(0, m + 1)] for i in range(0, m + 1)])
    b = numpy.array([sum([point[1] * (point[0] ** i) for point in points]) for i in range(0, m + 1)])
    c = numpy.linalg.solve(a, b)

    d0 = c[0]
    print('x =', x)
    print('f(x) =', f(x))
    print('Sm(x) =', horn(c, x, d0))
    print('|Sm(x) - f(x)| =', abs(horn(c, x, d0) - f(x)))


def horn(c, x0, di):
    for ci in c[0:]:
        di = ci + di * x0
    return di


least_squares(5, 4, 1, 5, 3)

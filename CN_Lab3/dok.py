import numpy as np
import sparse
from scipy import sparse


def dok(values):
    maxCol = len(values)
    datas = []
    for value in values:
        data = value
        datas.append(data)
        if len(data) > maxCol:
            maxCol = len(data)
    dokM = sparse.dok_matrix((len(values), maxCol))
    for i, data in enumerate(datas):
        for j, datum in enumerate(data):
            dokM[i, j] = datum
    return dokM

'''
def matrix():
    a = [[506.5,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,560.0,0,0,0,0,0,0,0],[13.5,0,0,0,0,0,0,0,0,0],[6.5,0,0,0,344.0,0,0,0,0,0],[0,0,16.0,0,0,0,0,0,0,0],[0,0,0,0,0,0,529.0,0,0,0],[0,0,21.0,0,0,0,19.0,0,0,0],[0,0,0,0,0,0,24.0,0,652.5,0],[14.5,0,0,0,0,0,0,0,0,0]]
    s = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

    for i in range (0,10):
        for k in range(0,10):
            for j in range(0, 10):
                if a[i][j] != 0 and a[j][k] != 0:
                    s[i][k] = s[i][k] + (a[i][j] * a[j][k])

    for i in range (0,10):
        print('')
        for j in range (0,10):
            print(s[i][j], '\t', end='')

'''

if __name__ == "__main__":
    val = [[1,2,3],[4,5,6],[7,8,9]]
    x = dok(val)
    print(x)

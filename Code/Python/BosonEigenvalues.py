import numpy as np
from numpy import linalg as LA


def MatrixElement(n, m, e, v):
    if(n-m == 0):
        return n*e
    elif n-m == 2:
        return np.sqrt(m+1)*np.sqrt(m+2)*(-v)
    elif n-m == -2:
        return np.sqrt(m)*np.sqrt(m-1)*(-v)
    return 0


def CreateMatrix02(n, e, v):
    m = []
    for i in range(n):
        line = []
        item_i = 2*(i)
        for j in range(n):
            item_j = 2*(j)
            res = MatrixElement(item_i, item_j, e, v)
            line.append(res)
        m.append(line)
    return m


def CreateMatrix13(n, e, v):
    m = []
    for i in range(n):
        line = []
        item_i = (2*i)+1
        for j in range(n):
            item_j = (2*j)+1
            res = MatrixElement(item_i, item_j, e, v)
            line.append(res)
        m.append(line)
    return m


def BosonMatrix(n, q):
    m_even = CreateMatrix02(n, 1, q)
    m_odd = CreateMatrix13(n, 1, q)
    m = [m_even, m_odd]
    return m

b0=BosonMatrix(3,1)[0]
b1=BosonMatrix(3,1)[1]

print(b0)
print(b1)
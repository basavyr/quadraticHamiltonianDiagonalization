import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt
from numpy import linalg as LA


def MatrixElement(n, m, e, v):
    if(n-m == 0):
        return n*e
    elif (n-m == 2):
        return np.sqrt(m+1)*np.sqrt(m+2)*(-v)
    elif (n-m == -2):
        return np.sqrt(m)*np.sqrt(m-1)*(-v)
    return 'Null'


def CreateMatrix02(n, e, v):
    m = []
    for i in range(n):
        line = []
        item_i = 2*(i)
        for j in range(n):
            item_j = 2*(j)
            res = MatrixElement(item_i, item_j, 1, 1)
            if(res != 'Null'):
                print(item_i, item_j, res)


def CreateMatrix13(n, e, v):
    m = []
    for i in range(n):
        line = []
        item_i = 2*i+1
        for j in range(n):
            item_j = 2*j+1
            res = MatrixElement(item_i, item_j, 1, 1)
            if(res != 'Null'):
                print(item_i, item_j, res)


CreateMatrix02(4, 1, 1)
print('')
CreateMatrix13(4, 1, 1)

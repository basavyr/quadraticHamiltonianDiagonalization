import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt
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
        item_i = 2*i+1
        for j in range(n):
            item_j = 2*j+1
            res = MatrixElement(item_i, item_j, e, v)
            line.append(res)
        m.append(line)
    return m


def CalculateEigenvalues(m):
    values, vectors = LA.eig(m)
    result = values
    return result


def CalculateEigenvectors(m):
    values, vectors = LA.eig(m)
    result = vectors
    return result


def LambdaQId(n, q, boson):
    if(boson == 0):
        matrix = CreateMatrix02(n, 1, q)
    else:
        matrix = CreateMatrix13(n, 1, q)
    results = []
    values = LA.eig(matrix)[0]
    for x in values:
        current_x = round(x, 4)
        results.append(current_x)
    return results


listOfSols = []
lambdaIndex = 1
for p in np.linspace(0, 3, 4):
    id = lambdaIndex-1
    lister = np.sort(LambdaQId(10, p, 0))
    lister = lister[id]
    listOfSols.append(lister)
# print(listOfSols)


# qValues = []
def GenerateQs(nqs):
    qValues=np.linspace(0, 3, nqs)
    return qValues

qValues=GenerateQs(3)

# print(qValues)

NQS=2

def LambdaEvolution(n, id, boson,nq):
    qValues=GenerateQs(nq)
    lambdas = []
    for q in qValues:
        ld = LambdaQId(n, q, boson)[id-1]
        # print(ld)
        lambdas.append(ld)
    return lambdas


def ShowSolutions(n,id):
    qValues2=GenerateQs(2)
    xs2=LambdaEvolution(n,id-1,0,2)
    qValues100=GenerateQs(100)
    xs100=LambdaEvolution(n,id-1,0,100)
    # for i in range(n):
    #     xs=LambdaEvolution(n,i,0)
    #     plt.plot(qValues,xs,'r-')
    plt.plot(qValues2,xs2,'r-')
    plt.plot(qValues100,xs100,'b-')
    plt.savefig('../../Reports/ldEvo.pdf', bbox_inches='tight')
    plt.close()

ShowSolutions(4,1)

# plt.plot(qValues, LambdaEvolution(10, 1, 0), '-r')
# plt.plot(qValues, LambdaEvolution(10, 2, 0), '-b')
# plt.plot(qValues, LambdaEvolution(10, 3, 0), '-b')
# plt.plot(qValues, LambdaEvolution(4, 3, 0), '-k')
# plt.plot(qValues, LambdaEvolution(4, 4, 0), '-m')


# m = CreateMatrix02(4, 1, 1)
# print(f'Eigenvalues')
# print(CalculateEigenvalues(m))
# print(f'Eigenvectors')
# print(CalculateEigenvectors(m))

# print(CreateMatrix02(4, 1, 1))
# print(CreateMatrix13(4, 1, 1))

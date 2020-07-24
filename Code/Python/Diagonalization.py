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
    qValues = np.linspace(0, 3, nqs)
    return qValues


qValues = GenerateQs(3)

# print(qValues)

NQS = 2


def LambdaEvolution(n, id, boson, nq):
    qValues = GenerateQs(nq)
    lambdas = []
    for q in qValues:
        ld = LambdaQId(n, q, boson)[id-1]
        # print(ld)
        lambdas.append(ld)
    return lambdas


pathPrefix = '../../Reports/'


def omega(q):
    return np.sqrt(1.0 - 4.0*(np.power(q, 2)))

qOmegas=np.linspace(0,0.5,100)
omegas=[]
for x in qOmegas:
    omegas.append(omega(x))

plotname=pathPrefix+'omegaCT.pdf'
plt.plot(qOmegas,omegas,'-b')
plt.savefig(plotname,bbox_inches='tight')
plt.close()

def ShowSolutions(n, id):
    nqReduced=4
    nqM=100
    for i in range(n):
        plotname=pathPrefix+'plot-id'+str(i+1)+'.pdf'
        fig, ax=plt.subplots()
        plt.xlabel('q')
        plt.ylabel(f'$\lambda_i$')
        ax.text(0.15, 0.75, f'$\lambda_{i+1}$ | N={n}', horizontalalignment='center',
                verticalalignment='center', transform=ax.transAxes)
        # ax.text(0.15, 0.85, f'$N={n}$', horizontalalignment='center',
        #         verticalalignment='center', transform=ax.transAxes)
        qValues_Red=GenerateQs(nqReduced)
        qValues_M=GenerateQs(nqM)
        xs_Red=LambdaEvolution(n, i+1, 0, nqReduced)
        xs_M=LambdaEvolution(n, i+1, 0, nqM)
        if(i+1 == id):
            print(f'Solution {id} for N={n}')
            print(f'Reduced | N={nqReduced}')
            print(qValues_Red)
            print(xs_Red)
            print(f'Accurate| N={nqM}')
            print(qValues_M)
            print(xs_M)
        ax.plot(qValues_Red, xs_Red, 'r-o', label=f'$n_d$={nqReduced}')
        ax.plot(qValues_M, xs_M, 'b-', label=f'$n_d$={nqM}')
        ax.legend(loc='best')
        plt.savefig(plotname, bbox_inches='tight')
        plt.close()


# ShowSolutions(10, 1)

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

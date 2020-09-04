import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt


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

# b0=BosonMatrix(3,1)[0]
# b1=BosonMatrix(3,1)[1]


def Eigensystem(n, q):
    matrix = BosonMatrix(n, q)
    b0 = matrix[0]
    b1 = matrix[1]
    values0 = list(LA.eigvals(b0))
    values1 = list(LA.eigvals(b1))
    # print(values0)
    # print(values1)
    values0.sort(reverse=True)
    values1.sort(reverse=True)
    print(values0)
    # print(values1)
    return [values0, values1]


def Eigensystem_Unordered(n, q):
    matrix = BosonMatrix(n, q)
    b0 = matrix[0]
    b1 = matrix[1]
    values0 = list(LA.eigvals(b0))
    values1 = list(LA.eigvals(b1))
    print(values0)
    # print(values1)
    return [values0, values1]

Eigensystem(10,1)
Eigensystem_Unordered(10,1)


def GetSolution(n, q, id):
    system = Eigensystem(n, q)
    return [system[0][id], system[1][id]]
    # print(system[0][id])
    # print(system[1][id])


def GetUnorderedSolution(n, q, id):
    system = Eigensystem_Unordered(n, q)
    return [system[0][id], system[1][id]]




def PlotLambda(n, id):
    filename = '../../Reports/LambdaPlots/LambdaBosonic-'+str(id+1)+'.pdf'
    qValues = np.arange(0, 3.1, 0.1)
    lambda02 = []
    lambda13 = []
    for q in qValues:
        x = GetSolution(n, q, id)
        lambda02.append(x[0])
        lambda13.append(x[1])
    fig, ax = plt.subplots()
    plt.xlabel(f'$q$')
    plt.ylabel(f'$\lambda$')
    plt.plot(qValues, lambda02, '-or', label=f'even-case')
    plt.plot(qValues, lambda13, '-ob', label=f'odd-case')
    plt.legend(loc='best')
    ax.text(0.15, 0.75, f'$\lambda_{id+1}$ | N={n}', horizontalalignment='center',
            verticalalignment='center', transform=ax.transAxes)
    plt.savefig(filename, bbox_inches='tight')


def PlotLambdaUnordered(n, id):
    filename = '../../Reports/LambdaPlots/LambdaDifference-'+str(id+1)+'.pdf'
    qValues = np.arange(0, 3.1, 0.1)
    lambda_0_ordered = []
    lambda_0_unordered = []
    for q in qValues:
        x_o = GetSolution(n, q, id)
        x_uno = GetUnorderedSolution(n, q, id)
        lambda_0_ordered.append(x_o[0])
        lambda_0_unordered.append(x_uno[0])
    fig, ax = plt.subplots()
    plt.xlabel(f'$q$')
    plt.ylabel(f'$\lambda$')
    plt.plot(qValues, lambda_0_ordered, '-or', label=f'ordered')
    plt.plot(qValues, lambda_0_unordered, '-ob', label=f'unordered')
    plt.legend(loc='best')
    ax.text(0.15, 0.75, f'$\lambda_{id+1}$ | N={n}', horizontalalignment='center',
            verticalalignment='center', transform=ax.transAxes)
    plt.savefig(filename, bbox_inches='tight')


# for id in range(10):
#     PlotLambdaUnordered(10, id)

# for id in range(10):
#     PlotLambda(10, id)

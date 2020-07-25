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

path='../../Reports/CleanPlots/'
filename=path+'cleanLambda'
ext='.pdf'

def LambdaEvolution(n,id):
    qValues=np.arange(0,3,0.05)
    lambdas=[]
    for q in qValues:
        bosonH=CreateMatrix02(n,1,q)
        values,vectors=LA.eig(bosonH)
        for x in range(len(values)):
            values[x]=np.float(round(values[x],3))
        print(q)
        print(values)
        # print(values[id])
        # lambdas.append(float(values[id-1]))
    # print(lambdas)
    # plt.plot(qValues,lambdas,'-b',label=f'$\lambda$')
    # plotname=filename+'-'+str(id)+ext
    # plt.savefig(plotname,bbox_inches='tight')
    # plt.close()

LambdaEvolution(10,1)
# LambdaEvolution(10,2)
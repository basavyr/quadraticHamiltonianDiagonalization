# algorithm for normalizing the vectors given by numpy eig

import numpy as np
from numpy import linalg as LA

m = [[0, 2, 1], [4, 2, 2], [1, 3, 0]]


def ComputeEigenvalues(matrix):
    values = LA.eig(matrix)[0]
    count = 1
    for l in range(len(values)):
        # print(f'Eigenvalue 𝝀[{count}]={values[l]}')
        count = count+1
    return values


def ComputeEigenvectors(matrix):
    vectors = LA.eig(matrix)[1]
    count = 1
    for l in range(len(vectors)):
        # print(f'Eigenvector v[{count}]={vectors[l]}')
        count = count+1
    return vectors


def CompareVectors(v1, v2):
    if(len(v1) != len(v2)):
        return 0
    count = 0
    for id in range(len(v1)):
        t1 = round(v1[id], 4)
        t2 = round(v2[id], 4)
        if(t1 == t2):
            count = count+1
    if(count == len(v1)):
        return 1
    return 0


def Eigen(matrix):
    values, vectors = [ComputeEigenvalues(matrix), ComputeEigenvectors(matrix)]
    for id in range(len(values)):
        vectorLA = vectors[:, id]
        l = values[id]
        vl = vectorLA*1
        # print(vl,vectorLA)
        # vm = np.matmul(matrix, vectorLA)
        # if(CompareVectors(vl, vm)):
            # print(f'The eigenvector and eigenvalue (With id={id}) are valid')
            # print(vm, vl)
    # print('Eigenvalues:')
    # print(values)
    # print('Eigenvectors:')
    # print(vectors)

# Eigen(m)

# print(ComputeEigenvectors(m))

# print(-1*np.matmul(m,ComputeEigenvectors(m)))
# print(ComputeEigenvectors(m)[:, 0])
# print(ComputeEigenvectors(m)[0])

m_symb = [['v_11', 'v_12', 'v_13'], [
    'v_21', 'v_22', 'v_23'], ['v_31', 'v_32', 'v_33']]
# print(m_symb[0])
# print(m_symb[1])
# print(m_symb[2])

x=ComputeEigenvectors(m)
print(x)
print(x[0])
print(x[1])
print(x[2])
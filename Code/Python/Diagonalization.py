import numpy
from numpy import random as rd
import matplotlib.pyplot as plt
from numpy import linalg as LA


def CreateMatrix02(n,e,v):
    m=[]
    for i in range(n):
        line=[]
        item_i=2*(i)
        for j in range(n):
            item_j=2*(j)
            item=[item_i,item_j]
            print(item)

def CreateMatrix13(n,e,v):
    m=[]
    for i in range(n):
        line=[]
        item_i=2*i+1
        for j in range(n):
            item_j=2*j+1
            item=[item_i,item_j]
            print(item)

CreateMatrix02(4,1,1)
CreateMatrix13(4,1,1)
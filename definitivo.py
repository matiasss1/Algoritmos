from types import NoneType
import numpy as np
from numpy.random import randn, rand, seed
import pandas as pd
import matplotlib.pyplot as plt
import math
from sympy import *
from scipy.spatial import distance

df = pd.read_csv("Matriz20.csv") #cargamos .csv
df = df.drop(df.columns[[0]], axis='columns') # borramos primera columna del .csv 

x = df.to_numpy()

g_sol = np.ndarray[0,1]
matriz_distancia = []
def funcion_distancia(i, j):
    distancia = distance.euclidean(i,j) # un punto
    return (distancia)

for e in range(len(x)):
    for k in range(len(x)):
        if e < k:
            punto1 = x[e][0],x[e][1]
            punto2 = x[k][0],x[k][1]
            d = funcion_distancia(punto1,punto2)
            matriz_distancia.append([punto1,punto2,d])
#print(matriz_distancia)
def fitness(i, j, d):
    H =  x[i]*x[j]*d
    return (H)
    
for e in range(len(x)):
    for k in range(len(x)):
        if e < k:
            dh = fitness(e,k,funcion_distancia(e,k))

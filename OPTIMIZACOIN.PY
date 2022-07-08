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
matriz_distancia = []
area = np.asarray([[0, 1.0]])

def funcion_distancia(i, j):
    distancia = distance.euclidean(i,j) # un punto
    return (distancia)

def funcino_objetivo(i, j, d):
    dotp = np.dot(i,j)
    H =  dotp * d
    return (H)

def dg(area,temperatura,iteraciones,tam_paso):
    punto1 = (x[0][0],x[0][1])

    aceptados=[]
    for s in range(iteraciones):
        candidate1 = punto1 + randn(len(area)) * tam_paso #vencidad
        candidate2 = punto2 + randn(len(area)) * tam_paso #vencidad
        
        #print("punto candidato:",candidate2[1])
        p_candidate1 = [candidate1[0],candidate1[1]]
        p_candidate2 = [candidate2[0],candidate2[1]]
        #print("punto candidato:",p_candidate2[0])
        candidate_eval = funcino_objetivo(p_candidate1,p_candidate2,funcion_distancia(p_candidate1,p_candidate2))

        diff = candidate_eval - pf
        t = temperatura / (float(s+1))
        metropolis = exp(-diff / t)
        if candidate_eval < pf:
            punto1 = p_candidate1
            punto2 = p_candidate2
            pf = candidate_eval
            aceptados.append(pf)
        else:
            if rand()<metropolis:
                punto1 = p_candidate1
                punto2 = p_candidate2
                pf = candidate_eval
                aceptados.append(pf)
        #print("if:",(punto1,punto2),pf,s)

    return [aceptados]
print(dg(area,10000,1000,0.1))

for e in range(len(x)):
    for k in range(len(x)):
        if e < k:
            punto1 = x[e][0],x[e][1]
            punto2 = x[k][0],x[k][1]
            d = funcion_distancia(punto1,punto2)
            matriz_distancia.append([punto1,punto2,d])
#print(matriz_distancia)

for e in range(len(x)):
    for k in range(len(x)):
        if e < k:
            dh = funcino_objetivo(e,k,funcion_distancia(e,k))


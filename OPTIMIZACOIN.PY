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
    H =  i*j * d
    return (H)

def dg(area,tam_paso):
    p1 = ((area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])),(area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])))
    #(1,2)
    p2 = ((area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])),(area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])))
    #(1,2)
    pf = funcino_objetivo(p1[0],p2[0],funcion_distancia(p1[0],p2[0]))
    #(1,2)
    curr1 = p1
    curr2 = p2
    #(1,2)(1,2)
    curr_eval = pf
    aceptados=[]
    c=0
    for s in range(len(x)):
        candidate1 = curr1 + randn(len(area)) * tam_paso #vencidad
        candidate2 = curr2 + randn(len(area)) * tam_paso #vencidad
        p_candidate1 = (candidate1[0][0],candidate1[1][0])
        p_candidate2 = (candidate2[0][0],candidate2[1][0])
        print("punto candidato:",p_candidate2)
        candidate_eval = funcino_objetivo(p_candidate1,p_candidate2,funcion_distancia((p_candidate1,p_candidate2),curr_eval))
        aceptados.append(candidate_eval)
        c=c+1
    return (aceptados,c)
dg(area,0.1)

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


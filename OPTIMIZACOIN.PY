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
    p1 = ((area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])),(area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])))
    #(1,2)
    #print('soy p1:',p1)
    p2 = ((area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])),(area[:, 0] + rand(len(area)) * (area[:, 1] - area[:, 0])))
    #(1,2)
    punto1 = p1[0][0],p1[1][0]
    punto2 = p2[0][0],p2[1][0]
    #print("punto1 ",punto1[0])
    distancia_p12 = funcion_distancia(punto1,punto2)
    pf = funcino_objetivo(punto1,punto2,distancia_p12)
    #print("distancia",distancia_p12)
    #print('soy pf:',pf)
    aceptados=[]
    c=0
    for s in range(iteraciones):
        candidate1 = punto1 + randn(len(area)) * tam_paso #vencidad
        candidate2 = punto2 + randn(len(area)) * tam_paso #vencidad
        #print("punto candidato:",candidate2[1])
        p_candidate1 = [candidate1[0],candidate1[1]]
        p_candidate2 = [candidate2[0],candidate2[1]]
        #print("punto candidato:",p_candidate2[0])
        candidate_eval = funcino_objetivo(p_candidate1,p_candidate2,funcion_distancia(p_candidate1[0],p_candidate2[0]))
        c=c+1
        diff = candidate_eval - pf
        t = temperatura / (float(s+1))
        metropolis = exp(-diff / t)
        if candidate_eval > pf and candidate_eval > 1:
            candidate1 = punto1
            candidate2 = punto2
            pf = candidate_eval
            aceptados.append(pf)
        else:
            if rand()<metropolis:
                candidate1 = punto1
                candidate2 = punto2
                pf = candidate_eval
                aceptados.append(pf)
        #print("if:",(punto1,punto2),pf,s)

    return [aceptados]
print(dg(area,10,1000,0.1))

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


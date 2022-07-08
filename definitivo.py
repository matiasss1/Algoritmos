import numpy as np
from numpy.random import randn, rand, seed
import pandas as pd
import matplotlib.pyplot as plt
from sympy import *
from scipy.spatial import distance

df = pd.read_csv("Matriz20.csv") #cargamos .csv
df = df.drop(df.columns[[0]], axis='columns') # borramos primera columna del .csv 

x = df.to_numpy()




area = np.asarray([[0, 1.0]])
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
            #matriz_distancia.append([punto1,punto2,d])
#print(matriz_distancia)

def fitness(i, j, d):
    H = i*j*d
    return (H)

def soluciones():
    aPunto_opt = []
    for e in range(len(x)):
        punto_optimo = x[e][0],x[e][1]
        aPunto_opt.append(punto_optimo)
    return aPunto_opt

def generar_vecino():
    numpy_float_arr = np.random.rand (1, 2)
    return numpy_float_arr

g = soluciones() # aca ira el punto optimo generado de la funcion solucion aleatoria

v = generar_vecino()
#v1 = v[0][0]
#v2 = v[0][1]

aZ = [] #arreglo de soluciones evaluadas en funcion optima

for e in range(len(g)):
    z = fitness(g[e][0],g[e][1], funcion_distancia(g[e][0],g[e][1])) #entregar solucion aleatoria
    aZ.append(z)
k = 0
kmax = 1000 
t = 1000
dT = 8
gn= 0 

while(k < kmax):
    G_vecino = generar_vecino() #generamos vecino a partir de nuestro punto optimo aleatorio
    v1 = G_vecino[0][0]
    v2 = G_vecino[0][1]  

    if gn < 21:
        Z_vecino = fitness(v1,v2, funcion_distancia((v1,v2),(g[gn])))#evaluamos g vecino en funcion optima
    else:
        gn = 0
    print("largo de z", z)
    print("soy z vecino", Z_vecino, "largo z vecino ")
    differencia = Z_vecino - z
    t = t / (float(k+1))
    metropolis = exp((- differencia)/t)
    print("yo soy metropolis", metropolis   )
    if Z_vecino < z:
       g = G_vecino
       z = Z_vecino
    else: 
        if rand() < metropolis:
          g = G_vecino
          z = Z_vecino 
    k=k+1
    gn=gn+21
    t=t*dT



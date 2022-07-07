import numpy as np
from numpy.random import randn, rand, seed
import pandas as pd
import matplotlib.pyplot as plt
import math
from sympy import *
import sympy
#Punto inicial =  fila 1 de cada .csv
#evaluar punto de inicio en funcion objetivo (sumatorias i hasta n, j hasta n Xi + Xj x Distancia euclidiana + [Sumatoria (X_i) hasta n x resticcion (quorum)] ** 2)
#Luego se asigna una variable para el punto inicial. y otra para el punto inicial evaluado en la funcion objetivo
# creamos un arreglo para guardar nuestras soluciones (11)
# ecuacion = i[m] * j[n] * dis + (i[m] * math.floor(len(i)/2) + 1)**2
df = pd.read_csv("Matriz20.csv") #cargamos .csv
df = df.drop(df.columns[[0]], axis='columns') # borramos primera columna del .csv 

df_i = df.drop(df.columns[[1]], axis='columns')
df_j = df.drop(df.columns[[0]], axis='columns')

i = df_i.values #guardamos valores de i en un arreglo
j = df_j.values #guardamos valores de j en un arreglo
plot_puntos = df.plot("0", "1", kind="scatter")

def funcion():
    for m in range(len(i)):
        for n in range(len(j)):
            p = [i[m],j[n]] # 1,1 1,2 ... 1, 20 , 2,1 2,2 2,3 ... 2,20 , 3,1 3,2 ,3,3... 3,20
            pe = [i[m], j[m]] # punto fijo 1,1 2,2 3,3, 4,4
            dis = math.dist(p,pe)
            ecuacion = i[m] * j[n] * dis + (i[m] * math.floor(len(n)/2) + 1)**2
            eval_p1 = i[0] * j[0] * dis + (i[0] * math.floor(len(n)/2) + 1)**2
            if dis > 1.0:   
                print("------------------------")
                print("Distancia euclidiana mayor q 1: ", dis)
                print("Arreglo variado en J q 1: ", p)
                print("Arreglo lineal mayor q 1: ", pe)
                plt.scatter(p, pe, marker= "*")
                plt.plot(p,pe,'ro-')
                plt.scatter(i[0], j[0], marker = "*")
    return [ecuacion] 

Area = np.asarray([[0, 1]])

def evaluacion(x, y, dit ,np):
    i = x
    j = y
    dis = dit
    n = np
    p = math.floor(n/2)
    f = i * j * dis + (i * p + 1)**2
    return f

def recocido(funcion_o, area, iteraciones, step_size, temp):
    p_inicial = i[0], j[0]
    p = evaluacion(i[0], j[0], 1.0, 20)
    p_i = p_inicial
    p_eval = p
    aceptado = []
    for i in range(iteraciones):
        paso = p_i + randn(len(area)) * step_size
        paso_e = 
    return 

recocido(funcion)
plt.show()
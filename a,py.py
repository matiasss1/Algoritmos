from turtle import distance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv("Matriz20.csv") #cargamos .csv
df = df.drop(df.columns[[0]], axis='columns') # borramos primera columna del .csv 

my_plot = df.plot("0", "1", kind="scatter")
#plt.show() 

df_i = df.drop(df.columns[[1]], axis='columns')
df_j = df.drop(df.columns[[0]], axis='columns')

i = df_i.values #guardamos valores de i en un arreglo
j = df_j.values #guardamos valores de j en un arreglo

p1 = [i[1], j[2]]
p2 = [i[19], j[19]]

for e in range(len(i)):
    for h in range(len(j)):
        #while i != j:
            dis = math.dist(i[e],j[h])
            if dis > 1.0:   
                print(dis)
                inicio = [i[0],j[1]]
                #plt.scatter(p, pe, marker= "*")
                #plt.scatter(i[0], j[0], marker = "*")
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 19:41:11 2022

@author: holas
"""

from numpy import asarray, exp
from numpy.random import randn, rand, seed
from matplotlib import pyplot

# Defino la funcion objetivo
def funcion(step):
    return step[0] ** 2.0

def sa(funcion_o, area, iterations, step_size, temperature): #son los parametros que utilizaremos
    punto_inicio = area[:, 0] + rand( len( area ) ) * ( area[:, 1] - area[:, 0] ) #punto inicio 
    print("aaa",punto_inicio)
    #print('punto inicio pr',punto_inicio)
    puntoi_eval = funcion_o(punto_inicio) #evaluo el punto inicio
    print("aaaaaaaaaaaaaaaa",puntoi_eval)
    #print("punto incio evaluado:",puntoi_eval)
    puntoi = punto_inicio  #asignamos las nuevas soluciones
    punto_ie = puntoi_eval #aqui igual
    outputs = [] 
    for i in range(iterations):
        paso = puntoi + randn( len( area ) ) * step_size #primer paso de mia  
        paso_e = funcion_o(paso) 
        if paso_e < puntoi_eval: #es menos al punto de inicio evaluado
            punto_inicio = paso 
            puntoi_eval = paso_e
            outputs.append(puntoi_eval) #guardamos los puntos aceptados 
            print('criterio de aceptacion =', mac," ",'numero de iteracion = ',i," ", 'mejor que= ',punto_inicio," " ,'nuevo mejor =', puntoi_eval)
        difference = paso_e - punto_ie #guardamos la diferencia
        t = temperature / float(i + 1) 
        mac = exp(-difference / t) #calculamos el criterio de aceptacion
        if difference < 0 or rand() < mac: #chequea si el punto ya se a aceptado
            puntoi = paso  
            punto_ie = paso_e
    return [punto_inicio, puntoi_eval, outputs]

seed(1) #El seed()método se utiliza para inicializar el generador de números aleatorios.
Area = asarray([[-6.0, 6.0]]) #definimos un area de busqueda
temp = 12 #temperatura incial
iteraciones = 1200 #numero total de iteraciones
T_paso = 0.1 #tamaño del paso
# perform the simulated annealing search
start_point, output, outputs = sa(funcion, Area, iteraciones, T_paso, temp) #retorna los 3 parametros 
#Graficamos
pyplot.plot(outputs, 'ro-')
pyplot.xlabel('Improvement Value')
pyplot.ylabel('Evaluation of Objective Function')
pyplot.show()

print('----------------------------------------------------------------')
print(start_point) 
print('----------------------------------------------------------------')
print(output)
print('----------------------------------------------------------------')
print(outputs)

# esta es la forma estandar de importar numpy
import numpy as np

 # Una lista de listas
matriz = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

nodos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

#Visualizacion de la matriz
print(matriz)

#Busacando el nodo con mayor numero de conexiones
nodo_mayor_suma = 0
nodo_mayor_vertices = 0
acumulado = 0
nodo = 0
for fila in matriz:
    for columna in fila:
        acumulado += columna
    if acumulado > nodo_mayor_suma:
        nodo_mayor_suma = acumulado
        nodo_mayor_vertices = nodo

    nodo +=1
    acumulado = 0


print("El nodo que mas tiene conexiones es:", nodos[nodo_mayor_vertices])
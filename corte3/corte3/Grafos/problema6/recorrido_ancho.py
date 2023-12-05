#AUTOR: Luis García
#CARRERA: Ingeniería en Computación

import os

#DEFINIENDO EL GRAFO MEDIANTE UN DICCIONARIO DE PYTHON:
#PARA MEJOR COMPRENSION EL VALOR 'a': [('p',4), ('j',15), ('b',1)],
#INDICA QUE EL VERTICE 'a' ES ADYACENTE CON 'P', CON 'J' Y CON 'b' 
#CADA UNO CON SU RESPECTIVO PESO, AUNQUE EL PESO PARA HACER RECCORRIDOS EN PROFUNDIDAD
#NO ES NECESARIO, SE LO AGREGUE PARA MOSTRAR TAMBIÉN LA IMPLEMENTACIÓN DE UN GRAFO PONDERADO

grafo = {'F': [('B',1), ('G',1)],
         	'B': [('A',1), ('J',1), ('D',1)],
			'D': [('C',1), ('E',1)],
			'G': [('I', 1)],
			'I': [('H',1)],
			'A': [('B', 1)],
			'C': [('D', 1)],
			'E': [('D', 1)],
			'J': [('B', 1)],
			'H': [('I', 1)]
		}


#MUESTRA EL GRAFO ANTES DEL RECORRIDO
print("Muestra el grafo antes del recorrido: \n")
for key, lista in grafo.items():
	print(key)
	print(lista)

print()
os.system("pause")
		
visitados = []
cola = []

origen = input("Ingresa el nodo origen: ")
print("\nLista de recorrido en anchura\n")
#Paso 1: SE COLOCA EL VÉRTICE ORIGEN EN UNA COLA
cola.append(origen)
#Paso 2: MIENTRAS LA COLA NO ESTE VACÍA
while cola:
	#paso 3: DESENCOLAR UN VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
	actual = cola.pop(0)

	#paso 4: SI EL VÉRTICE ACTUAL NO HA SIDO VISITADO
	if actual not in visitados:
		#paso 5: PROCESAR (IMPRIMIR) EL VÉRTICE ACYZLUAL
		print("Vertice actual -> ", actual)
		#paso 6: COLOCAR VÉRTICE ACTUAL EN LA LISTA DE VISITADOS
		visitados.append(actual)
	#paso 7: PARA CADA VÉRTICE QUE EL VÉRTICE ACTUAL TIENE COMO DESTINO,
	#        Y QUE NO HA SIDO VISITAO:
	#        ENCOLAR EL VERTICE
	for key, lista in grafo[actual]:
		if key not in visitados:
			cola.append(key)

print()
os.system("pause")
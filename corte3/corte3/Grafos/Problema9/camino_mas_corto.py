from Dijsktra import *
from os import system
Oficinas=["A","B","C","D","E"]
aristas=[
        ("A","B",3),
        ("B","D",6.5),
        ("B","C",4.3),
        ("C","E",3.5),
        ("D","E",4.5)
]
g=build_graph(aristas)
def calcular():
    origen=input("Ingrese la oficina de origen: ")
    destino=input("Ingrese la oficina de destino: ")
    peso=int(input("Ingrese el peso del paquete: "))
    d, prev = dijkstra(g, origen, destino)
    valor=(peso)/150*2000*d
    print("El valor del envio es: ",valor)

def menu():
    print("1. Factura")
    print("2. Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        calcular()
    elif opcion==2:
        system("cls")
        exit()
    else:
        print("Opcion invalida")
menu()

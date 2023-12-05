from Dijsktra import *
from os import system

archivos_cargados = False


#Obteniendo informacion del txt solicitudes
list_solicitudes = []

solicitudes_usuarios = []

usuarios = []

#Oficinas
oficinas = ["A", "B", "C", "D", "E", "F", "G", "H"]
solicitudes_realizadas = [0, 0, 0, 0, 0, 0, 0, 0]

#Construccion del grafo
aristas = [
        ("A", "B", 3),
        ("A", "C", 1),
        ("B", "D", 1),
        ("B", "G", 5),
        ("C", "D", 2),
        ("C", "F", 5),
        ("D", "F", 2),
        ("D", "E", 4),
        ("E", "H", 1),
        ("E", "G", 2),
        ("F", "H", 1)
]


def cargarArchivos():
    fsolicitudes = open("solicitudes.txt", "r")
    lineasarchivo = fsolicitudes.readlines()
    fsolicitudes.close()

    for linea in lineasarchivo:
        documento = linea.split(":")[0]
        info_solicitud = linea.split(":")[1].split(",")

        nombre = info_solicitud[0]
        direccion = info_solicitud[1].removesuffix("\n")

        list_solicitudes.append([documento, nombre, direccion])
        solicitudes_usuarios.append(nombre)
        if nombre not in usuarios:
            usuarios.append(nombre)
    archivos_cargados = True

def calcularTotalDiasDocumentos():

    g = build_graph(aristas)
    total_dias = 0
    
    for solicitud in list_solicitudes:
        d, prev = dijkstra(g, "A", solicitud[2])

        nombre_archivo = "Tickets/"+ "A" + solicitud[0] + ".txt"
        fticket = open(nombre_archivo, "a")
        fticket.write("Solicitud: Enviar documento a la oficina " + solicitud[2] + " el tiempo en llegar son " + str(d) + " dias\n" )
        fticket.close()

        total_dias += d
    
    print("El total de dias por todos los documentos es", total_dias)
                  
def estadistica_oficinas():
    for solicitud in list_solicitudes:
        destino_solicitud = solicitud[2]
        solicitudes_realizadas[oficinas.index(destino_solicitud)] += 1
    
    for oficina in oficinas:
        print("Oficina", oficina + ":")
        print("Solicitudes:", solicitudes_realizadas[oficinas.index(oficina)], "\n")


def estadistica_usuarios():
    for usr in usuarios:
        print(usr, "realizo", solicitudes_usuarios.count(usr), "solicitudes")

#Menu principal

def menu():
    print("""
    1) Cargar solicitudes.
    2) Calcular dias para todos los documentos.
    3) Generar estadistica de documentos requeridos por oficina.
    4) Generar estadistica de numero de solicitudes por usuario.
    5) Salir

    """)

while(True):
    system("clear")
    
    menu()

    opcion = input("Elija una opción: ")

    while not archivos_cargados:
        
        if opcion == "1":
            cargarArchivos()
            archivos_cargados = True
        elif opcion == "5":
            break
        else:
            print("¡primero cargue los archivos!")
        opcion = input("Elija una opción: ")

    match opcion:

        case "1":
            cargarArchivos()
            opcion = input("Presione enter para continuar")
        
        case "2":
            calcularTotalDiasDocumentos()
            opcion = input("Presione enter para continuar")
        
        case "3":
            estadistica_oficinas()
            opcion = input("Presione enter para continuar")
        
        case "4":
            estadistica_usuarios()
            opcion = input("Presione enter para continuar")
        
        case "5":
            break
        
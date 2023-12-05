farchivos_transacciones = open("transacciones.txt", "r")
lista_transacciones = farchivos_transacciones.readlines()
farchivos_transacciones.close()

estudiantes = []
estudi_creditos = []

estudiantes_mejor_promedio = []

respuesta = []
promedio_creditos = 0

for linea in lista_transacciones:
    info_estudiante = linea.split(";")
    codigo = info_estudiante[0]
    apellidos = info_estudiante[1]
    nombres = info_estudiante[2]
    creditos = int(info_estudiante[3].removesuffix("\n"))
    promedio_creditos += creditos

    estudiantes.append(apellidos + " " + nombres)
    estudi_creditos.append(creditos)

promedio_creditos = promedio_creditos/len(estudiantes)

for cred in estudi_creditos:
    if cred > promedio_creditos:
        estudiantes_mejor_promedio.append(cred)

respuesta.append(len(estudiantes_mejor_promedio))

for estu in estudiantes_mejor_promedio:
    respuesta.append(estu)
    
respuesta = tuple(respuesta)

print(respuesta)



import json

transacciones = {}

#Obteniendo transacciones
ftransacciones = open("transacciones.json", "r")
transacciones = json.load(ftransacciones)
ftransacciones.close()

#Buscando al estudiante con mayor número de creditos
mayor_creditos = 0
cod_estudiante = ""

for codigo in transacciones.keys():
    if transacciones[codigo]["Creditos"] > mayor_creditos:
        mayor_creditos = transacciones[codigo]["Creditos"]
        cod_estudiante = codigo

#Generando respuesta
estudiante_mayor_creditos = {cod_estudiante:transacciones[cod_estudiante]}

festudiante = open("estudiante.json", "w")
json.dump(estudiante_mayor_creditos, festudiante, indent=4)
festudiante.close()
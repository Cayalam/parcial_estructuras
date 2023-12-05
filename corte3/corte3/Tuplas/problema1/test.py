
#Diccionarios 
datosUsuarios = {}
establecimiento = {"1":"1101"}
numeros_cuenta = {"1010":"8902392323-24"}

#Obteniendo datos del usuario
fdatos_usuarios = open("datosCliente.txt", "r")
listaLineas = fdatos_usuarios.readline()
fdatos_usuarios.close()

info_usuario = listaLineas.split(";")
tarjeta = info_usuario[0].split(":")[1]
valor_compra = int(info_usuario[1].split(":")[1])
cod_datafono = info_usuario[2].split(":")[1]
fecha = info_usuario[3].split(":")[1]

if valor_compra > 0 and valor_compra < 100000:
    comision = (valor_compra*0.5)/100

elif valor_compra > 100001 and valor_compra < 1000000:
    comision = (valor_compra*0.4)/100

elif valor_compra > 1000000:
    comision = valor_compra/100
else:
    print("El valor de la compra debe ser mayor que cero")
print("Comision:", comision)

#Tuplas
codigo_establecimiento = establecimiento[cod_datafono]
numero_cuenta = numeros_cuenta[tarjeta]


tupla_estabecimiento = (codigo_establecimiento, comision, valor_compra - comision)
tupla_banco = (numero_cuenta, valor_compra)

fdatos_usuarios = open("datosCliente.txt", "w")
fdatos_usuarios.write("Tarjeta:;ValorCompra:;Datafono:;Fecha:")
fdatos_usuarios.close()

print("Tupla establecimiento:", tupla_estabecimiento)
print("Tupla banco:", tupla_banco)
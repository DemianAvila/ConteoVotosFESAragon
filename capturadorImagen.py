#conseguir las imagenes de cada documento de identificación
from importarID import *

#variable para controlar el flujo de ingreso de datos
contador=0

#leer el documento donde estan los resultados
resultadosVotacion=open("./resultadosVotacion.csv", "r")

#importar modulo para encargarse de vocales con modificadores
from caracteresEspeciales import caracteresEspeciales

#diccionario que almacena los datos introducidos por el usuario
introducidosUsuario={
    "nombre": "",
    "correo": "",
    "carrera":"",
    "docIdentificacion":"",
    "paro":"",
    "agregarPuntos":"",
    "actualizarPliego":"",
    "removerCargo":"",
    "transparentarVotos":"",
}


#iterar sobre cada resultado
for voto in resultadosVotacion:
    #ignora la primera linea
    if voto.startswith("Marca temporal"):
        continue
    datosVoto=voto.split(',')

    #vaciar los datos en el diccionario para comparar
    introducidosUsuario["nombre"]=caracteresEspeciales(datosVoto[4])
    introducidosUsuario["correo"]=datosVoto[1]
    if "INGENIERIA" in caracteresEspeciales(datosVoto[2]):
        carreraSinGenerico=caracteresEspeciales(datosVoto[2]).rstrip("INGENIERIA").strip()
        introducidosUsuario["carrera"]=carreraSinGenerico
    else:
        introducidosUsuario["carrera"]=caracteresEspeciales(datosVoto[2])
    introducidosUsuario["docIdentificacion"]=datosVoto[3]
    introducidosUsuario["paro"]=datosVoto[5]
    introducidosUsuario["agregarPuntos"]=datosVoto[6]
    introducidosUsuario["actualizarPliego"]=datosVoto[7]
    introducidosUsuario["removerCargo"]=datosVoto[8]
    introducidosUsuario["transparentarVotos"]=datosVoto[9].rstrip()

    print(introducidosUsuario)
    print(f"{contador}/20")

    obtenerDocumento(introducidosUsuario["docIdentificacion"], contador)
    contador+=1
    if contador==46: break

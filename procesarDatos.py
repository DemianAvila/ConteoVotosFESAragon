#para observar si existe determinado archivo en una carpeta
import os


#convertir imagen a texto
from convertirImagenATexto import textoCrudo

#todas las validaciones necesrias para el documento
from validaciones import *

#importar modulo para encargarse de vocales con modificadores
from caracteresEspeciales import caracteresEspeciales

#variable para controlar el flujo de ingreso de datos
contador=0

#leer el documento donde estan los resultados
resultadosVotacion=open("./resultadosVotacion.csv", "r")


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

while contador<47:

    for voto in resultadosVotacion:

        #ignora la primera linea
        if voto.startswith("Marca temporal"):
            continue

        banderaArchivo=False
        while banderaArchivo==False:
            #intenta encontrar la imagen con el contador actual
            if os.path.isfile(f"{contador}.png"):
                banderaArchivo=True
            #si si existe, permite que el flujo continue


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

        #la información del documento se almacena aqui
        infoDocumento={
            #historial, comprobante o no identificado
            "tipoDocumento":"",
            "coincideNombre":"",
            "estudianteActivo":"",
            "carreraValida":"",
            "coincideCarrera":"",
        }

        #ya existe el screenshot
        #aplicarle ocr
        texto=textoCrudo(f"{contador}.png")
        texto=caracteresEspeciales(texto)

        #tipo de documento
        infoDocumento["tipoDocumento"]=tipoDocumento(texto)

        #coincide nombre con los documentos?
        infoDocumento["coincideNombre"]=coincideNombre(texto, introducidosUsuario["nombre"])

        #status de estudiante
        infoDocumento["estudianteActivo"]=statusEstudiante(texto, infoDocumento["tipoDocumento"])

        #verificar carrera
        tmp=carreraValida(texto, infoDocumento["tipoDocumento"], introducidosUsuario["carrera"])
        infoDocumento["carreraValida"]=tmp["carreraValida"]
        infoDocumento["coincideCarrera"]=tmp["coincideCarrera"]

        print(infoDocumento)
        print (f"{contador}/20")



        coma=","

        if (infoDocumento["tipoDocumento"]=="NO IDENTIFICADO") or (infoDocumento["estudianteActivo"]=="SOSPECHOSO") or (infoDocumento["carreraValida"]==False) or (infoDocumento["coincideCarrera"]==False) or (infoDocumento["coincideNombre"]!=True):

            #vaciar los resultados en dos archivos
            #crear el archivo de errores si no existe
            if os.path.isfile("errores.csv")==False:
                errores=open("errores.csv", "w")
                campos=[]
                data=[]
                for i in introducidosUsuario:
                    campos.append(i)
                    data.append(introducidosUsuario[i])
                campos=coma.join(campos)
                campos=campos+"\n"
                errores.write(campos)
                data=coma.join(data)
                data=data+"\n"
                errores.write(data)
            else:
                errores=open("errores.csv", "a")
                data=[]
                for i in introducidosUsuario:
                    data.append(introducidosUsuario[i])
                data=coma.join(data)
                data=data+"\n"
                errores.write(data)

        else:
            #crear el archivo de no errores si no existe
            if os.path.isfile("noErrores.csv")==False:
                noErrores=open("noErrores.csv", "w")
                campos=[]
                data=[]
                for i in introducidosUsuario:
                    campos.append(i)
                    data.append(introducidosUsuario[i])
                campos=coma.join(campos)
                campos=campos+"\n"
                noErrores.write(campos)
                data=coma.join(data)
                data=data+"\n"
                noErrores.write(data)
            else:
                noErrores=open("noErrores.csv", "a")
                data=[]
                for i in introducidosUsuario:
                    data.append(introducidosUsuario[i])
                data=coma.join(data)
                data=data+"\n"
                noErrores.write(data)



        os.remove(f"{contador}.png")
        contador+=1

import re


def tipoDocumento (texto):
    #2 posibilidades
    #la cadena de texto crudo incluye las palabras "comprobante de reinscripción", en cuyo caso se trata de ese documento
    #la cadena de texto incluye las palabras "historia academica" en cuyo caso es ese documento
    # no incluye ninguna de esas 2 cadenas, no se descarta como documento, pero adquiere el estatus de documento no identificado
    if "HISTORIA ACADEMICA" in texto:
        tipo="HISTORIA ACADEMICA"
    elif "COMPROBANTE DE REINSCRIPCION" in texto:
        tipo="COMPROBANTE DE REINSCRIPCION"
    else:
        tipo="NO IDENTIFICADO"

    return tipo

#coincide nombre
#regresa una tupla o una condicion de verdadero; es decir, la tupla es para ver si el nombre se halla en el documento o cuantos fragmentos de nombre se hallan
def coincideNombre (texto, nombreIntroducido):
    fragmentos=nombreIntroducido.split()
    totalFragmentos=len(fragmentos)
    fragmentosCoincidentes=0
    for fragmento in fragmentos:
        if fragmento in texto:
            fragmentosCoincidentes+=1
    if fragmentosCoincidentes==totalFragmentos:
        return True
    else:
        return (fragmentosCoincidentes, totalFragmentos)


#regresa si un estudiente es activo o sospechoso
#si el documento es comprobante de inscripción, debe contener el patrón 2021-11
#si el documento es historial el año de ingreso debe ser mayor a 2017, o si no, es sospechoso
def statusEstudiante(texto, tipoDoc):
    if tipoDoc=="COMPROBANTE DE REINSCRIPCION":
        if ("2021-11" in texto)==True:
            return "ACTIVO"
        else:
            return "SOSPECHOSO"
    elif tipoDoc=="HISTORIA ACADEMICA":
        #obten el año de entre todo el texto
        try:
            inicioAnio=texto.index("AÑO")
            anio=""
            while texto[inicioAnio]!="\n":
                try:
                    int(texto[inicioAnio])
                except ValueError:
                    inicioAnio+=1
                    continue
                anio=anio+texto[inicioAnio]
                inicioAnio+=1
            anio=anio.strip()
            anio=int(anio)
        except: anio=0

        try:
            #obten los creditos, si el numero es mayor a 90, que sea sospechoso y valida de forma manual
            inicioCreditos=texto.index("TOTALES")
            creditos=""
            while texto[inicioCreditos]!="%":
                creditos=creditos+texto[inicioCreditos]
                inicioCreditos+=1
            backwards=-1
            numCreditos=""
            while creditos[backwards]!=" ":
                numCreditos=numCreditos+creditos[backwards]
                backwards-=1

            numCreditos=numCreditos.strip()
            numCreditos=numCreditos[::-1]
            try:
                numCreditos=float(numCreditos)
            except:
                numCreditos=100
        except: numCreditos=100

        #valida que el año no sea sospechoso
        if anio<2017 or numCreditos>90:
            return "SOSPECHOSO"
        else:
            return "ACTIVO"
    else: return "SOSPECHOSO"

#carrera
#revisa si la carrera que ingresaron coincide con la de su papel
#en caso de su carrera pertenezca a las que ya no estan en paro o del SUAyED, el voto es tomado como cancelado
#retorna 2 valores, coincide carrera y carrera valida como booleanos
def carreraValida (texto, tipoDoc, carreraDoc):
    listaCarreras={
    "COMUNICACION Y PERIODISMO":["1612"],
    "DERECHO":["1325"],
    "ECONOMIA":["1382"],
    "PLANIFICACION PARA EL DESARROLLO AGROPECUARIO":["2092"],
    "RELACIONES INTERNACIONALES":["1275"],
    "SOCIOLOGIA":["1324"],
    "ARQUITECTURA":["0186"],
    "DISEÑO INDUSTRIAL":["1082"],
    "PEDAGOGIA":["1103"],
    "CIVIL":["1280"],
    "EN COMPUTACION":["1279","2119"],
    "ELECTRICA Y ELECTRONICA":["1312"],
    "INDUSTRIAL":["1313","1347","1348"],
    "MECANICA": ["1314", "1349", "1350", "1351", "1352", "1353"],
    }
    #checar la carrera de cualquiera de los documentos
    coincideCarrera=False
    carreraValida=False
    #iterar todas las carreras
    for carrera in listaCarreras:
        #iterar todas las claves
        for clave in listaCarreras[carrera]:
            #si el tipo de documento es historia académica
            if tipoDoc=="HISTORIA ACADEMICA":
                """
                inicioCarrera=texto.index("CARRERA")
                carreraHist=""
                #delimita en el texto donde esta la carrera
                while texto[inicioCarrera]!="\n":
                    carreraHist=carreraHist+texto[inicioCarrera]
                    inicioCarrera+=1
                #si el nombre de la carrera proporcionado por el alumno y la clave del plan de estudios de la carrera estan en el archivo, la carrera coincide
                print(carreraHist)"""

                if carreraDoc in texto:
                    coincideCarrera=True
                    if clave in texto:
                        carreraValida=True
                    #carrera definitiva
                    carreraDef=carreraDoc
                #si la clave no coincide, se puede tratat de un alumno de SUA


            elif tipoDoc=="COMPROBANTE DE REINSCRIPCION":
                #verificar palabra por palabra de la carrera
                carreraFrag=carreraDoc.split()
                fragmentos=len(carreraFrag)
                fragmentosCoincidentes=0
                for fragmento in carreraFrag:
                    if fragmento in texto:
                        fragmentosCoincidentes+=1
                if fragmentosCoincidentes==fragmentos:
                    coincideCarrera=True
                    if clave in texto:
                        carreraValida=True
                    carreraDef=carreraDoc

            else: carreraDef=None

            #checar que no se metan carreras que ya no estan en paro
            #quitar a las ingenierias
            noEnParo={
                "CIVIL":"1280",
                "ELECTRICA Y ELECTRONICA":"1312",
                "MECANICA": ["1314", "1349", "1350", "1351", "1352", "1353"],
            }
            for cNoEnParo in noEnParo:
                try:
                    if cNoEnParo==carreraDef:
                        carreraValida=False
                except: pass

    return {
        "coincideCarrera":coincideCarrera,
        "carreraValida":carreraValida
    }

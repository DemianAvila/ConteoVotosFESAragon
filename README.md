# PROGRAMA DE CONTEO DE VOTOS PARA LA ENCUESTA DE LA FES ARAGON

## Funcionamiento

1.- Toma el .csv que contiene los datos de los votantes de la FES Aragon, uno a uno; esos datos son vaciados en un diccionario

2.- Dentro de ese diccionario está el link para acceder al google drive que contiene el documento de identificación

3.- Con Web Scrapping se accede de forma automática a cada uno de los documentos y se les captura en imagen 

4.- A la captura de la imagen se le aplica OCR para convertir la imagen a texto crudo

5.- A partir de diferentes tecnicas de tratamiento de texto crudo se obtienen los datos de los alumnos que son comparados a lo que ellos pusieron en la encuesta, arrojando si el voto puede ser validado o si necesita ser revisado manualmente

** ** 

**OJO: ESTE PROGRAMA NO TIENE CONTRA QUE COMPARAR LOS DATOS, NO SE TIENE ACCESO A NINGUNA BASE DE DATOS PROPIA DE LA UNAM; SOLO SIRVE PARA EFICIENTAR EL PROCESO DE SELECCIÓN DE VOTOS VALIDOS Y NO VALIDOS**
** **

Los criterios que se usan para discernir si un voto es o no valido es si cumple con las siguientes caracteristicas:

* Si el nombre insertado coincide con el que muestra el documento
* Si no se pertenece a alguna de las carreras que no está en paro
* Si se es alumno activo 
  * En el caso de un comprobante de inscripción, el documento lo dice de forma explicita
  * En el caso de un historial académico, si el año de ingreso es abajo del 2017, o el numero de creditos es mayor a 90% de forma automatica debe pasar a revisión manual

* Si un documento no es legible con claridad o si este se muestra recortado de alguno de los puntos que se utilizan en recoleccion de datos
  * En este sentido, el programa tiene sesgos; si el documento fue subido en captura de pantalla desde movil, foto al monitor o en general cualquier factor que disminuya la calidad de la imagen o haga chico el tamaño de las letras el software no podrá leerlo y pasará a revisión manual
  
** **

** Ninguna foto o documento permanece en el ordenador personal de quien ejecute este programa, pues está programado para autodestruir la imagen una vez que se ha terminado de usar **

** **
Los resultados correctos e incorrectos se guardan en diferentes archivos excel, los votos que sean cancelados serán publicados junto con el motivo y sus respuestas de acuerdo al punto correspondiente de la encuesta
****
Cualquier duda, dirigirse a Facebook @Mesa-Estudiantil-FES-Aragón
Repositorio publicado en GitHub para auditoría bajo Licencia Creative Commons Atribución 4.0 Internacional.

#las fechas es la representacion de un tiempo, en python podemos sincronizar datos enviarlos junto con su fecha.
#Esto no es algo propio de python y por eso se debe importar librerias dentro del mismo python

from datetime import datetime #Importamos la funcion datetime del modulo datetime

hora = datetime.now() #inicalizamos un funcion dentro de datetime que nos indicara la hora actual y lo guardamos en una variable
print(hora.day)
print(hora.month)
print(hora.day)
print(hora.hour)
print(hora.minute)
print(hora.second)

timestamp=hora.timestamp()
print(timestamp); 
#Aclaracion el timestamp es una forma de codificar el momento donde se ejecuta el codigo,
#por ejemplo, si queremos enviar la fecha  y otra, no enviamos el dia, el mes , el año, la hora, los minutos, etc.
#Sino que directamente enviamos el codigo que genera el timestamp y el receptor decodifica ese valor y sabe que fecha y que hora es.
#Si queremos guardar la fecha de algo, guardamos el timestamp, por ejemplo, y no la fecha en su formato tradicional.


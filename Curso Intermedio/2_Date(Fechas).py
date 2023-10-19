#las fechas es la representacion de un tiempo, en python podemos sincronizar datos enviarlos junto con su fecha.
#Esto no es algo propio de python y por eso se debe importar librerias dentro del mismo python

from datetime import datetime #Importamos la clase datetime del modulo datetime

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

#Yo tambien puedo guardar una fecha, ya sea futura o pasada
fecha_nueva = datetime (2023, 12 , 25) #año, mes y dia.
print(fecha_nueva)


#----------------------------------------------------------------------------------------

from datetime import time #Ahora importamos la clase time, del modulo (libreria) datetima

current_time=time()

print(current_time.hour)
print(current_time.minute)
print(current_time.second) #aca los 3 nos da 0, porque la clase time, no se vincula a la hora actual, sino que nosotros
                            #debemos cargar la hora que nosotros queramos.

current_time=time(21,5,26) #Hora, minuto, segundo
print(current_time.hour)
print(current_time.minute)
print(current_time.second)#Aca si nos muestra los valores que pre cargamos anteriormente


#------------------------------------------------------------------------------------------------------------------------

from datetime import date 

current_date = date(2024, 5, 23) #lo mismo para date que para time, son funciones para representar una fecha, pero deben ser pre cargadas.
print(current_date.year)
print(current_date.month)
print(current_date.day)

#Estas funciones al principio no parece ser muy utiles pero sirven para precargar y guardar fechas y horas.
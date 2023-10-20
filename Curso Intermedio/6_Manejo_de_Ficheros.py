#Ficheros de archivos TXT

#Para abrir un fichero utilizamos la operacion Open

fichero = open("fichero.txt","r") #El r es para poder leerlo, si queremos escribir usariamos el comando w
print(fichero.read())               #Para leer y escribir ponemos w+
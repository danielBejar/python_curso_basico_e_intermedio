#Ficheros de archivos TXT

#Para abrir un fichero utilizamos la operacion Open

archivo = open("fichero.txt","r")   #El r es para poder leerlo, si queremos escribir usariamos el comando w
print(archivo.read())               #Para leer y escribir ponemos w+
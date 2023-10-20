#ficheros de archivos TXT

#Para abrir un fichero utilizamos la operacion Open

entrada = open("fichero.txt","r")  #El r es para poder leerlo, si queremos escribir usariamos el comando w
                                    #Para leer y escribir ponemos w+
print(entrada.read())              #lee el txt de forma completa, si no se ejecuta nada, hay que entrar desde la terminal a la carpeta donde esta el archivo.py C:\Users\danielsan\Dropbox\VSCODE\python\Curso_Intermedio> (Verificar que la terminal este en la carpeta correcta)

#print(entrada.read (10))           #Solo imprime los primeros 10 caracerere (comentar el print anterior para que funcione)

#print(entrada.readline())          #Imprime la primera linea (comentar el print anterior para que funcione)

#print(entrada.readlines())         #Coloca cada linea dentro de un vector (comentar el print anterior para que funcione)

#Aclaracion importante, cuando usamos la funcion read() lo que hace el es crear un puntero que apunta hacia la primera direccion del
#documento txt. EJ: si nosotros utilizamos el comando entrada.readline() 2 veces seguidas mostrará las 2 primeras lineas
#Y si al final utilizamos el readlines() el solamente colocara en forma de vector las lineas restantes del documento txt.
#Es  por eso que aca comentamos y descomentamos las lineas de codigo para ejecutar otros comandos de  la funcion read()

#Ej, ejecutamos el comando read()

#print(entrada.read())  #Lo que hace este entrada es leer todo el txt
                        #Si nosotros ejecutamos  abajo un readlines() no va a leer todo el txt de nuevo, directamente no va a mostrar nada
                        #Debido a que cuand el read() que ejecutamos antes coloco el puntero al final del documento txt.
#print("vector vacio:",entrada.readlines()) #Este comando no mostraria nada, debido a que el primer entrada.read() dejo el puntero al final del txt.


#Para escribir debemos usar el comendo w al cargar
salida= open("fichero2.txt","w") 
salida.write("\n Texto agregadoooo") #El \n es para que escriba en la linea siguiente y no pegado a la ultima linea

#Aclaracion, si no existe el archivo fichero2.txt el VA A CREARLO.

#Cuando usamos la funcion open lo que hacemos es abrir el fichero desde python, lo que se debe hacer al finalizar de
#leer o escribir en un fichero es cerrarlo. 

entrada.close() #Cerramos los ficheros usados
salida.close()

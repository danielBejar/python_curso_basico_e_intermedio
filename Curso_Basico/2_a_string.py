strin1= "Hola"
Strin2= " mundo"

texto = strin1 + Strin2 
print ("1-----",texto)

texto2= "podemos agregar otro texto a " + texto 
print ("2-----",texto2)

#Se puede ir recorriendo el stream de a pasos [start: stop: step]
print ("2-----",strin1[0])      #Muestra el primer caracter de string
print ("3-----",strin1[0:4])    #Muestra desde el caracter 0 al caracter 4
print ("4-----",strin1[0:4:2])  #Muestra desde el caracter 0 al caracter 4 de 2 en 2 osea muestra el caracter 0,2,4,6
print ("5-----",texto2[::-1])   #Muestra el texto de atras para adelante
print ("6-----",texto2.upper()) #La funcion upper convierte todo el texto en mayusculas
print ("6-----",texto2.split()) #La funcion upper devuelve cada texto separado por elementos


#Las listas no necesariamente tienen que solo letras, pueden ser letras y numeros.
Lista=[1,2,3, "lista"]
print("1-----",Lista)
print("1-----",Lista[-1])   #Muestra el ultimo valor de la lista
print("1-----",Lista[:])    #Muestra toda la lista



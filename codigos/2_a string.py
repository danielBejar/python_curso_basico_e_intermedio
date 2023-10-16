strin1= "Hola"
Strin2= " mundo"

texto = strin1 + Strin2 
print (texto)

texto2= "podesmos agregar otro texto a " + texto 

print (texto2)

print (strin1[0]) #Muestra el primer caracter de string
print (strin1[0:4]) #Muestra desde el caracter 0 al caracter 4
print (strin1[0:4:2]) #Muestra desde el caracter 0 al caracter 4 de 2 en 2 osea muestra el caracter 0,2,4,6
print (texto2[::-1]) #Muestra el texto de atras para adelante

#Las listas no necesariamente tienen que solo letras, pueden ser letras y numeros.

Lista=[1,2,3, "lista"]
print(Lista)
print(Lista[-1]) #Muestra el ultimo valor de la lista
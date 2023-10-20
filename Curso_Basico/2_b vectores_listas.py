lista_1 = [1,2,3,4,4.5,"ASD"] 
print ("1--------", lista_1[0]) #muestra el valor de la lista_1 en la primera posicion


#Para agregar un valor al final de la lista_1 usamos el comando append
lista_1.append(6) #agrega un 6 al final de la lista_1
print ("2------", lista_1)


#Para unir dos lista_1s
lista_2 = [5,6,7,8,9]
lista_1.extend(lista_2) 		#Une la lista_1 a la lista_2
print("3------",lista_1)


#Tambien se puede sumar las lista_1s.
lista_2_1=lista_2 + lista_1
print("4------",lista_2_1)

#Para agregar un elemento en una posicion especifica,
#Para eso usamos el comando insert
lista_1.insert(1,1.5) #Aca agrega el valor 1.5, antes de la posicion 1, es decir antes del valor 2. 
                    #recordar que las posiciones empiezan en 0, lista_1[0]=1 , lista_1[1]=2
print("5------",lista_1)


#Para saber si tenemos un valor dentro de nuestra lista_1, usamos el comando in
print("6------",10 in lista_1) #Aca muestra con un true o un false, si el numero 10 esta dentro de la lista_1
print("7------",9 in lista_1) #Mostraria un true porque hay un 9 en la lista_1

#Tambien podemos buscar un valor dentro de la lista_1 y saber en que posicion esta, usando el comando index
print("8------",lista_1.index(1)) #Muestra la POSICION de donde se encuentra el valor 10
print("9------",lista_1.index(3)) #Nos devuelve un 0, porque el uno esta en la posicion 0. lista_1[0]=1

#Tambien podemos pedir cuantos valores tenemos repetidos dentro de la lista_1. para eso usamos la funcion count
print("10------",lista_1.count(6)) #Nos devuelve un 2, debido a que en la lista_1 3 ahora tenemos dos 6.


#Tambien podemos borrar elementos de las lista_1. Para ello usamos la funcion pop
lista_1.pop() #Borra el ultimo valor de la lista_1
lista_1.pop(0) #Borra el primer valor de la lista_1
print ("11------",lista_1)

#Podemos usar tambien la funcion remove, que elimina todos los valores dentro de la lista_1.
lista_1.remove('ASD') #Borra valor "ASD" de la lista_1, sin importar su ubicacion
print ("12------",lista_1) 
#Aclaracion: si tenemos valores repetidos, borra el primer valor que encuentre en la lista_1. de izquierda a derecha

#Para invertir la lista_1 , usamos el comando reverse
lista_1.reverse()
print ("13------",lista_1) 

#Ademas de sumar tambien podemos duplicarlo o triplicarlo
lista_1= lista_1 *2
print ("14------",lista_1) 

#podemos ORDENAR una lista_1, para ello usamos el comando sort
lista_1.sort() #Ordena de menor a mayor
print ("15------",lista_1) 

#Si queremos ordenar de mayor a menor, usamos la funcion reverse
lista_1.sort(reverse=True) #Ordena de mayor a menor
print ("16------",lista_1) 

#Para borrar toda la lista_1, usamos el comando clear
lista_1.clear() #Borra toda la lista_1
print ("17------",lista_1)

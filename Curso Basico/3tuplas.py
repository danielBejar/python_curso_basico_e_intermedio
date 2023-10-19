#Los tuples son como listas pero no se pueden modificar, agregar valores o eliminar valores y van entre parentesis

T= (1,2,3, "asd")
print ("1------",T)

#T[0]=2   #Aca el compilador me salta error debido a que yo quiero modificar una lista tople


#Tambien podemos modificar una lista comun y convertirla en un tuple
lista=[1,2,3,4,5,"dsa"]
T=tuple(lista) #Ahora la lista paso a ser una tuple y esta no puede ser modificada.
print ("2------",T)


#Se puede buscar dentro de una tuple, con el comando in

print("3------",3 in lista) #Aca devuelve un true o un false, si hay un 3 dentro de la tuple llamada lista


#podemos buscar la posicion donde esta un valor, usando el comando index
print("4------",lista.index(4)) #me devuelve la posicion donde esta el valor 4

#podemos pedir que nos busque cuantos elementos tenemos dentro de la lista
print("5------",lista.count(3))#Nos devuelve la cantidad de veces que se repite 3

#podemos saber cuantos elementos tiene una tuple, para ello usamos la funcion len
print("6------",len(lista)) #muestra la cantidad de elementos tiene la tupla

#podemos cambiar la tupla en una lista y ahi si podriamos modificarla.

lista = list(lista) #Ahora es una lista y se puede modificar
lista = lista * 2
print("7------",lista)

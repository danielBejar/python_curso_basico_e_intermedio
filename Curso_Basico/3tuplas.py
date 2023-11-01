#Los tuples son como listas pero no se pueden modificar

T1= (1,2,3, "asd") #la tupla T ya no se puede modificar
print ("1------",T1)

#No hace falta poner el parentesis, pero es conveniente.
T2= 1, 2, 3, 4, 5, 6 
print ("2------",T2)
print ("2/1------",type(T2)) #Vemos que a T2 se le dio el valor tupla 
#T[0]=2   #Aca el compilador me salta error debido a que yo quiero modificar una lista tople


#Tambien podemos modificar una lista comun y convertirla en un tuple
lista=[1,2,3,4,5,"dsa"]
Tupla_1=tuple(lista) #Ahora la lista paso a ser una tuple y esta no puede ser modificada.



#Se puede buscar dentro de una tuple, con el comando in

print("3------",3 in Tupla_1) #Aca devuelve un true o un false, si hay un 3 dentro de la tuple 


#podemos buscar la posicion donde esta un valor, usando el comando index
print("4------",Tupla_1.index(4)) #me devuelve la posicion donde esta el valor 4

#podemos pedir que nos busque cuantos elementos tenemos dentro de la lista
print("5------",Tupla_1.count(3))#Nos devuelve la cantidad de veces que se repite 3

#podemos saber cuantos elementos tiene una tuple, para ello usamos la funcion len
print("6------",len(Tupla_1)) #muestra la cantidad de elementos tiene la tupla

#podemos cambiar la tupla en una lista y ahi si podriamos modificarla.

lista = list(Tupla_1) #Ahora es una lista y se puede modificar
lista = lista * 2
print("7------",lista)

#las tuplas tambien se puede guardar en distintos elementos.
A, B , C, D = 12, 32, 43, 54
print("8------",A,B,C,D)

#dentro de las listas podemos tener funciones, ya sea while, for, que nos pueden servir para recorrer esa lista
#copiar esa lista o mostrar valores dentros de las listas.

mi_lista = [0, 1, 2, 3, 4, 5 , 6 ,7 , 8, 9]

#Para copiar esa lista podemos hacer lista_copia=mi_lista, pero esta es una forma muy basica de hacerlo
#Ademas no siempre se quiere copiar todos los elementos, a veces solo se quiere copiar algunos.
#Para ello se puede realizar una lista que dentro de esta lista tenga una funcion.

lista_copia = [i for i in mi_lista] #copia todos los valores de la lista en la lista copia
print("1------",lista_copia)

#Tambien se puede recorrer por rango. Ej: los primeros 5 valores

lista_copia = [i for i in range(5)] #solamente copiamos los primeros 5 valores de la lista
print("2------",lista_copia)

#Podemos copiar solo los numeros enteros

lista_copia = [i%2 for i in mi_lista] #indica que elementos de mi_lista es par o no (si es par = 0, si es impar es =1)
print("3------",lista_copia)

lista_copia = [i*2 for i in mi_lista] #multiplica cada valor de la lista * 2
print("4------",lista_copia)

#Tambien podemos poner funciones dentro de una lista

def  numeros_pares (numero): #Esta funcion devuelve el valor solamente si es un numero par
    if numero%2==0:
        return numero #solamente devuelve si el numero es par, sino retornaria un None
    #else: return("-") 
    
lista_copia = [numeros_pares(i) for i in mi_lista]
print("5------",lista_copia)

#podemos  hacerlo todo en una sola linea de codigo

filtrado = [x for x in mi_lista if x % 2 != 0]
print("5------",filtrado) 
my_set = set ([1,2,2,3,4,"palabra"])
print("1------",my_set)

my_set2={1,2,2,3,4}
print(type(my_set2))
print("2------",my_set2)

my_set3={"palabra2", "palabra1", "palabra3"}
print("3------",my_set3) #se mostrara en el orden que el quiera.


#Podemos buscar un elemento dentro del set
print("3------", 3 in my_set) #Aca devuelve un true o un false, si hay un 3 dentro del set

#Para borrar un elemento 
my_set.remove(1) #Borra el valor 1, dentro del set
print("4------", my_set) 

#Para unir dos set.
my_set4=my_set.union(my_set3)
print("5------", my_set4) 

#Para borrar un set entero
my_set.clear() #Borra todo  el set
print ("6------",my_set)

#agregar un elemento a un set
my_set4.add("Nueva palabra")
print ("7------",my_set4)

#borrar un elemento en especifico
my_set4.discard("Nueva palabra")
print ("8------",my_set4)

#interseccion de dos sets
print("9------",my_set4.intersection(my_set3)) #Devuelve los valores que sean iguales de ambos set


		
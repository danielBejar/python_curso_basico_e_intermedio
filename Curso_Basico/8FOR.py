#recorrer una lista con un for
lista=[10,20,30,40,50]
for i in lista: #El in indica que el contador i va a tomar los valores de la lista. RECORDAR SIEMPRE PONER EL ":"
    print(i,"", end="")



#EEl valor de i no tiene que ir subiendo o bajando, simplemente indica que valor va a tener i en la siguiente vez que se inicie el for
print()
for i in [1,1,1]:
    print(i,"", end="")  #el valor i solo valdrá 1 para todos los caso del for


#Los valores i no necesariamente tienen que ser numeros fijos, sino que tambien puede ser la cantidad de una letra o palabra. EJ:
print()
lista= "Monitor"
for i in lista:
    print(i,"", end="")  #Lo que hace este for es muestra la palabra monitor letra por letra, cave destacar que los valores de i ahora son letras no numeros



#No hace falta crear una lista, podemos insertar la palabra directamente
print()
for i in "ejemplo":
    print(i,"", end="")  #Aca muestra la palabra ejemplo, una por una mientras recorre el for, cave destacar que los valores de i ahora son letras no numeros



#Supongamos que queremos es hacer un rango o que se ejecute dentro de unos determinados valores . Ej: i<3
print()
for i in range (10):
    print(i,"", end="") #Aca recorre los valores de i desde el 0 a 3 , que en este caso es 0 1 2


#Ahora supongamos que queremos ingresar un valor que determine el rango . por ejemplo que i<x, siendo x=5
print();
#x=int(input("Ingrese el valor de X:"))
x=10
for i in range(x):
    print(i,"", end="") 
    if i>4:
        break #El break lo hace aca es romper el for, y cuando i=5, termina el ciclo
              #mostrando unicamente los valores 0 1 2 3 4 5

#si queremos que el contador del fort recorra cada elemento de una lista
print()
my_list = [32,24,62,18,27]

for element in my_list:
    print(element,"", end="") 

#Tambien se puede utilizar un for para recorrer un diccionario
print()
d1 = {'a': 1, 'b': 2, 'c':'3', 'd':4}
for elemento in d1:
    if elemento=='c':
      print(elemento,":",d1['c']) #imprime el valor c del diccionario d1

#--------------------------------------------------------------------------------------------------------------------

#Ejemplo: suponemos que queremos poner los valores al cuadrado de una lista dentro de otra
lista1=[1,2,3,4,5]
lista2=[]

for i in lista1: #el valor i a recorrer cada valor de la lista1
    lista2.append(i**2) #agrega el valor de i al cuadrado en lista2
print(lista2,"",end="")

#otra forma es poner el for dentro de la lista cuado se declara la funcion
print()
lista3=[i**2 for i in lista1]
print(lista3,"",end="")
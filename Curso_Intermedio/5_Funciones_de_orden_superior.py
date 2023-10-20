#funciones de orden superior, son basicamente funciones que tienen funcionen dentro de ellas.

def suma(num1, num2):
    return (num1 + num2)

def resta(num1, num2):
    return (num1 - num2)

def funcion_superior(numero1, numero2): #Ejemplo de una funcion de orden superior
    valor=suma(numero1,numero2)
    print("El valor de la suma es", valor)

funcion_superior(5,6)

#Tambien podemos enviar funciones  a otras funciones

def funcion_superior2(numero1, numero2, operacion): #Aca enviamos los dos valores y la funcion suma
    return operacion(numero1,numero2)

print(funcion_superior2(5,6,suma)) #se le envia los valores y ademas se le envia la funcion suma
print(funcion_superior2(5,6,resta))

#FUNCIONES CLOSURES ------------------------------------------------------------------------------
#las funciones tambien pueden retornar funciones

def contador(): #funcion principal
    def sumador(numero): #funcion secundaria que suma un valor al valor recibido
        return (numero +1) 
    return(sumador) #retur de la funcion principal, que retorna una funcion

bandera=contador() #recordar que la funcion contador devuelve una funcion, es decir que bandera no es una variable
                    #sino que es una funcion tambien.

numero=0
while numero<10:
    numero= (bandera(numero)) #a la funcion bandera = funcion sumador, se le suma un valor hasta llegar al 10
    print(numero, end=" ")
   

#------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE ORDEN SUPERIOR  PROPIAS DE PYTHON

def duplicador(num):
    return num*2

#Funcin MAP --------------------------------------

#En Python, la función map nos permite aplicar una función sobre los items de un objeto iterable (lista, tupla, etc...). 
# La función retornará un objeto map que posteriormente podemos convertir a una lista o tupla. 
# Es posible utilizar map junto con una función lambda.

numeros=[2,4,6,8,10]

numeros_duplicados = map(duplicador,numeros) #Enviamos tanto la funcion duplicador como la lista nuermos
print()
print("1---------",numeros_duplicados) #Aca vemos la funcion map devuelve una direccion de memoria, por eso se debe convertir
                               #El valor de retorno de map en una lista para mostrarla.

numeros_duplicados = list(map(duplicador,numeros)) # apuntamos esa direccion de maps a una lista 
print("2---------",numeros_duplicados)


#Funcion Filter ----------------------------------------------------------
# La función filter() integrada de Python puede usarse para crear un nuevo iterador a partir de un iterable existente (como una lista o un diccionario) 
# que filtrará de forma eficiente los elementos usando una función que proporcionamos.
#  Un iterable es un objeto Python que puede “repetirse” es decir, devolverá elementos en una secuencia de forma que podamos usarla en un bucle for.

def filter_numeros_pares(valor):
    if valor%2 == 0: #pregunta si el numero es par
        return valor

numeros_enteros=[1,2,3,4,5,6,7,8,9,10]
numero_pares=list(filter(filter_numeros_pares,numeros_enteros)) #De nuevo la funcion filter devuelve un puntero, para convertir en una lista los valores que
                                                                #apunta ese punto se usa la funcion list()
print("3---------",numero_pares)

#Tambiien lo podemos hacer una lambda para no estar definiendo funciones fuera del codigo

numero_pares=list(filter(lambda lista: lista%2 == 0, numeros_enteros))
print("4---------",numero_pares)

#explicaciones del codigo anterior.
#el codigo anterior lo que hace es que llama a la funcion filter, esta funcion en ves de enviar una funcion y la lista (numeros_enteros)
#se crea la funcion directamente dentro del filtro con el comando lambda (funcion sin nombre), la funcion lambda recibe un parametro "lista"
# que en este caso es un vector y pregunta si cada valor de lista es par o no (no hace falta poner if para ello) y retorna si el numero es par solamente
#El valor de "lista" es igual a 'numeros_enteros', pero se puede hacer con cualquier vector.
#Estos valores filtrados por el comando filter, son colocados en una lista y guardados en la variable "numeros_pares".

otra_lista=[1,2,3,2,4,5,1,34,7,5,22,6]
numero_pares=list(filter(lambda lista_lambda: lista_lambda%2 == 0, otra_lista)) #aca mandamos otra lista
print("5---------",numero_pares)
#Recordar, la funcion lambda recibe una variable que se llama "lista_lambda" = "otra_lista", y pregunta
#si cada valor de esa lista es par, si es true devuelve ese valor comparado.

#con esto no ahorramos muchas lineas de codigo. No hace falta crear una funcion aparte y el if
#se encuentra implicito despues de escribir "lista_lambda: ............. "

#-----------------------------------------------------------------------------------------------------------------------------

#Funcion Reduce ---------------------------------------
# toma como argumento un conjunto de valores (una lista, una tupla, o cualquier objeto iterable) y lo "reduce" a un único valor
#A partir de Python 3 la función fue movida al módulo estándar functools
from functools import reduce

nueva_lista=[1,2,3,2,4,5,1,34,7,5,22,6]
print("6---------", reduce(suma, nueva_lista)) #Devuelve el valor de todos los valores de nueva_lista sumados

#aclaracion, lo que hace reduce es que suma 1 + 2 =3 y eso lo suma a 3 que da como resultado 6
#ese valor de 6 le suma 2 y asi sucesivamente.

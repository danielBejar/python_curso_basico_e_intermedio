#Las expresiones lambda en Python son una forma corta de declarar funciones pequeñas y anónimas (sin nombres).
#Las funciones Lambda se comportan como funciones normales declaradas con la palabra clave def. Resultan útiles cuando se desea definir una función pequeña de forma concisa.
# Pueden contener solo una expresión, por lo que no son las más adecuadas para funciones con instrucciones de flujo de control.

#Forma tradicional de hacer una funcion
def sumar(numero1, numero2):
    return (numero1+numero2)

#Forma de hacerlo en forma anonima (lambda)
sum = lambda numero1,numero2: numero1 + numero2  #funcion anonima sin nombre detro de una variable

print(sum(3,4)) #retorna un 7 que es la suma de ambos numeros.

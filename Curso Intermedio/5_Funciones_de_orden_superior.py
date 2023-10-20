#funciones de orden superior, son basicamente funciones que tienen funcionen dentro de ellas.

def suma(num1, num2):
    return (num1 + num2)

def funcion_superior(numero1, numero2): #Ejemplo de una funcion de orden superior
    valor=suma(numero1,numero2)
    print("El valor de la suma es", valor)

funcion_superior(5,6)

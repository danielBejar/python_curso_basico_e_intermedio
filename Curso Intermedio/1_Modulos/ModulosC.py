from ModulosA import sumar #Aca importamos la funcion sumar del modulo (libreria) "ModulosA"

valor=sumar(2,3)
print("El valor de la suma es:",valor)

#Si la el modulo tiene mas de un funcion, tendremos que poner
#from ModulosA import sumar
#from ModulosA import restar
#from ModulosA import etc

#Pero hay otra forma mas facil y es poner directamente

from ModulosA import * #Al poner el asterisco importamos todas las funciones del moduloA
#Aclaracion: esto lo que hace es reservar todo el espacio de memoria, porque carga todas las
#funiones dentro del modulo, por eso no se recomienda hacerlo si solamente vas a usar una funcion o dos.

valor=multiplicar(2,3)
print("El valor de la multiplicacion es es:",valor)

#Aca estamos trabajando con funciones, pero se puede usar estructuras, tuplas, clases , etc.

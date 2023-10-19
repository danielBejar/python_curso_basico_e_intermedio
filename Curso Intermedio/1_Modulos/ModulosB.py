#Desde aca llamamos al  modulo que creamos en el punto 1_a

import ModulosA

valor=ModulosA.sumar(2,3) #Llamamos a la funcion sumar detro del modulo ModulosA
print("El valor de la suma es:",valor)

#Para no tener que poner siempre ModulosA.sumar..... se puede importar directamente la funcion
#Sin tener que estar escribiendo el nombre del modulo cada vez que se necesite usar la funcion
#Ver el moduloC
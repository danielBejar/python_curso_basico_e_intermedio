

#Estrutura IF
numero=int(input("Ingrese un valor:"))
if numero>0:
    print ("El numero es mayor a 0")
else:
        if numero==0:
            print("El numero es igual a 0 ")
        else:
            print("El numero es menor a 0")

#otra de usar el IF 
if numero>0:
	print ("El numero es mayor a 0")
elif numero==0:  # Elif es como un if que se ejecuta en caso de que el primer if, no se cumpla
	print("El numero es igual a 0 ")
elif numero!=0:   
     print("El numero no es igual a cero") #Los elif se pueden concatenar, es decir, que si no se cumple el primer IF, se ejecutara el primer elif	
										 	#Si no se ejecuta el primero elif se ejecutara el segundo elif
else:
    print("El numero es menor a 0")

numero2=int(input("Ingrese un valor:"))

if 10<numero2<20:
	print("el valor ingresado se encuentra dentro del rango")
      
else: print("El numero ingresado no se encuentra dentro del rango")
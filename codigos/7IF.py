

#Estrutura IF
numero=int(input("Ingrese un valor:"))
if numero>0:
    print ("El numero es mayor a 0")
else:
        if numero==0:
            print("El numero es igual a 0 ")
        else:
            print("El numero es menor a 0")

## otra forma seria poner 
if numero>0:
    print ("El numero es mayor a 0")
elif numero==0:  # Elif es como un if que se ejecuta en caso de que el primer if, no se cumpla
     print("El numero es igual a 0 ")
else:
    print("El numero es menor a 0")
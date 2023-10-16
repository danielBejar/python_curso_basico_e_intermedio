numero=10;
print (numero)
while numero>0: #VA : al final del while 
        numero=numero-1
        print(numero,"", end="") 

#en python podemos hacer while para que trabaje con condicion

condicion=True
while condicion: #este while lo que hace es repetir hasta que se ingrese un numero negativo
        print()
        m=int(input("ingrese numero:"))
        if m<0:
                condicion=False
                print(condicion)
                print("el numero ingresado es negativo! ")

        else: print("el numero ingresado es positvo! ")
        print(condicion)
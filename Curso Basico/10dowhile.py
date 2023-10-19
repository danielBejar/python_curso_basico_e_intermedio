#En python no existe la estructura do while, python la elimino. Pero se puede hacer con estructura while un do while.
#Una forma sencilla es haciendo una condicion de true o false al comienzo con otro while

x=0
condicion=True

while condicion==True: #No hace falta poner condicion==True, con poner solamente "while condicion:" funciona
    x=x+1
    print(x,"", end="") 
    if x>3:
        condicion=False

#La gracia del do while es que el comando se ejecute al menos una vez y asi se hace en python.

#Otra forma es poner un brak, el break hace que se rompa cualquier estructura repetitiva cuando es llamada.
condicion=True
x=0
print()
while condicion: #Aca no pusimos condiccion==True, pero anda igual. La magia de python es que todo funcione siempre :)
    x=x+1
    print(x,"", end="") 
    if x>3:
        break #El break rompe todo


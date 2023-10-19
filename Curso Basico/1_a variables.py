curso= "Hola mundo"
print (curso)
#Podemos cambiar el valor de curso y pasar de un string a un entero sin problemas
curso=-100
print(type(curso))

print(11 // 2)

print ("Hola" + "Pythom" + "3")       	#Suma string dentro de la funcion print
		
print (3 <= 4)			#Suma enteros dentro de la funcion print

name, surname, age = "Nombre" , "Apellido" , 30
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age)) #Forma 1 de imprimir varias varibales
print("Mi nombre es %s  %s y mi edad es %s" %(name, surname, age))

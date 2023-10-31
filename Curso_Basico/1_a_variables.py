curso= "Hola Mundo"
print("1 ------",curso)
#Podemos cambiar el valor de curso y pasar de un string a un entero sin problemas
curso=-100.0
print("2 ------",type(curso))

print("3 ------",11 // 2)  #Divion entera

print ("4 ------","Hola" + "Pythom" + "3")       	#Suma string dentro de la funcion print
print("5 ------","palabra 1" != "palabra 2") #imprime un true o un false si son distintas las palabras		

print ("6 ------",3 <= 4)			#Suma enteros dentro de la funcion print
print("7 ------","test" in "testing") #pregunta si la palabra test se encuentra dentro de la palabra testing

name, surname, age = "Nombre" , "Apellido" , 30
print("8 ------","Mi nombre es {} {} y mi edad es {}" .format(name, surname, age)) #  Forma 1 de imprimir varias varibales
print("9 ------","Mi nombre es %s  %s y mi edad es %s" %(name, surname, age))

#-----------------------------------------------------------------------------------------
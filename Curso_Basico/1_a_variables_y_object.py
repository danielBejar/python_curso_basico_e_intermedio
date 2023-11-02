#VARIABLES ---------------------------------------------------------------------------------------------------------------------------------------
#	Las variables en python no necesitan ser declaradas como en los lenguajes de bajo nivel. Simplemente con declararla e igualarla ya esta definida.
#	Las variables siempre tienen que deben declararse en MINUSCULA y debe estar unida por guion bajo, no por guio medio, punto, @, etc.

number = 576  			        #Declaramos un entero
float_number = 7.5		    	#Declaramos un float
country = "Este es un string" 	#Asi se declara un string
city = 'A'			        	#Declaramos un char
first_name = 'Daniel Fernando'	#se puede usar tanto '' o ""	
status = False 			        #declaramos una variable de tipo bool	

#Mutar variables --------------------------------------------------------------------------
curso= "Hola Mundo"
print("1 ------",curso)
#Podemos cambiar el valor de curso y pasar de un string a un entero sin problemas
curso=-100.0
print("2 ------",type(curso))

#Operaciones con variables ----------------------------------------------------------------
print("3 ------",11 // 2)                        #Divion entera
print("3 ------",3 ** 2)                         #hace 3^2
print ("5 ------","Hola" + "Pythom" + "3")    	 #Suma string dentro de la funcion print
print("6 ------","palabra 1" != "palabra 2")     #imprime un true o un false si son distintas las palabras		
print ("6 ------",3 <= 4)			             #Coparar enteros enteros dentro de la funcion print
print("7 ------","test" in "testing")            #pregunta si la palabra test se encuentra dentro de la palabra testing


#Variables en conjunto ------------------------------------------------------------------
#Las variables se pueden crear en conjunto [Esto esta mal y no cumple con la codificacion PEP8, la forma correcta es hacerlo linea a linea]
name, surname, age = "Nombre" , "Apellido" , 30
print("8 ------","Mi nombre es {} {} y mi edad es {}" .format(name, surname, age)) #Forma 1 de imprimir varias varibales
print("9 ------","Mi nombre es %s  %s y mi edad es %s" %(name, surname, age))

#Variables de tipo OBJECT --------------------------------------------------------------
#En Python, una variable de tipo "object" se refiere a una variable que ha sido asignada a un objeto, pero no se ha especificado un tipo específico
#para ese objeto. En Python, los objetos pueden pertenecer a diferentes clases y tipos, y la variable de tipo "object" 
#se utiliza para representar un objeto genérico sin restricciones en cuanto a su tipo.

mi_variable = object()
print(type(mi_variable))
#En este caso, mi_variable es una variable que se ha asignado a un objeto genérico de tipo "object". \
#Puedes asignarle cualquier objeto, como una lista, una cadena, un entero, etc., ya que no se imponen restricciones en 
#cuanto al tipo de objeto que puede contener.
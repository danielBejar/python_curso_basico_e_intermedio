#Las clases en python se definen con el comando class

class nueva_clase:
    alumnos={"Apellido:":"", "Nota:":""}  #esta clase tiene un objeto llamado alumnos (un diccionario) con dos parametros Apellido y Nota

    #Las funciones dentro de las clases son los METODOS 
    def __init__(self):     #La funcion _init se usa cuando queremos inicializar algun atributo (constructor en c++)
                            #debe tener 2 GUIONES BAJOS antes y despues de cada init
        self.alumnos["Apellido:"]= "ninguno"
        self.alumnos["Nota:"]=0        
        print("Objeto nuevo creado")
        print(self.alumnos)
        
    def carga(self,A,B): #Las funciones (metodos) en un clase, no puede tener elementos vacios, como minimo deben tener un seft
        self.alumnos["Apellido:"]=A #Carga la variable A(nombre del alumno) en el diccionario
        self.alumnos["Nota:"]=B  #Carga la variable B(nota) en el diccionario
        print(self.alumnos) #muestra el diccionario cargado



C=nueva_clase() #creamos una nueva clase y la llamamos C

A=input("Ingrese el apellido del alumno:")
B=input("Ingrese la nota del alumno:")
C.carga(A,B)

#---------------------------------------------------------------------------------------------------------

#otro ejemplo de clases

class curso: 
        def __init__(self,curso:str , cantidad: int): #Aca lo que hacemos es inicializar la clase curso, ya pidiendo valores de entrada un str y un entero
                   self.nombre_del_curso=curso   
                   self.cantidad_alumnos=cantidad   #Lo que hicimos aca es que para inicializar una clase se tenga que pasar 2 valores
                                                    #Se debe pasar un nombre y un entero para inicializar esta clase.


curso1=curso(input("ingrese el nombre del curso:",), input ("Ingrese la cantidad de alumnos:",)) #se crea la nueva clase y se el envia los parametros
print(curso1.nombre_del_curso)
print(curso1.cantidad_alumnos)    
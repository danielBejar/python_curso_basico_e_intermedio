class Clase:
    alumnos={"Alumno:":"", "Nota:":""}  

    def __init__(self): #Las funciones dentro de las clases son los METODOS  
                        #La funcion _init se usa cuando queremos inicializar algun atributo (constructor en c++)
                        #debe tener 2 GUIONES BAJOS antes y despues de cada init
        print("Objeto nuevo creado")

    def carga(self,A,B):
        self.alumnos["Alumno:"]=A #Carga la variable A(nombre del alumno) en el diccionario
        self.alumnos["Nota:"]=B  #Carga la variable B(nota) en el diccionario
        print(self.alumnos) #muestra el diccionario cargado

C=Clase()
A=input("Ingrese el apellido del alumno:")
B=input("Ingrese la nota del alumno:")
C.carga(A,B)

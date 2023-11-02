#las clases en python pueden heredar atributos y metodos de otras clases.

class Persona ():
    def __init__(self, nombre_recibido, apellido_recibido, edad_recibida):
        self.nombre=nombre_recibido     #se iguala el nombre recibido al atributo nombre de la clase persona
        self.apellido=apellido_recibido #idem
        self.edad=edad_recibida         #idem
    
    def mostrar(self): #Las funciones (metodos) en un clase, no puede tener elementos vacios, como minimo deben tener un seft 
        print("El nombre del alumno es",self.nombre, "y su apellido es:", self.apellido)

#Aclaracion: aca no se creo ningun atributo antes de la funcion __init__, la creacion de los atributos nombre, apellido y edad se hizo de 
#manera implicita dentro de __ini__

#HERENCIA-----------------------------------------------------------

class Alumno(Persona): #Ahora la clase Alumno, recibe todos los metodos y atributos de la clase persona
    curso="nombre del curso"
    año="año del alumno"
    def __init__(self, *datos, curso_recibido, año_recibido):
        super().__init__(*datos)
        self.curso=curso_recibido
        self.año=año_recibido
        


persona1 = Persona("daniel","bejar", 25)
persona1.mostrar()

alumno1 = Alumno("Curso B","1er Año")
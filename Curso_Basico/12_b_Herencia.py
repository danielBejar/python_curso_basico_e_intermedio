#las clases en python pueden heredar atributos y metodos de otras clases.

#CLASE PADRE
class Persona (): 
    def __init__(self, nombre_recibido, apellido_recibido, edad_recibida):
        self.nombre=nombre_recibido     #se iguala el nombre recibido al atributo nombre de la clase persona
        self.apellido=apellido_recibido #idem
        self.edad=edad_recibida         #idem
    
    def mostrar(self): #Las funciones (metodos) en un clase, no puede tener elementos vacios, como minimo deben tener un seft 
        print("El nombre del alumno es",self.nombre, "y su apellido es:", self.apellido, "y su edad es", self.edad)

#Aclaracion: aca no se creo ningun atributo antes de la funcion __init__, la creacion de los atributos nombre, apellido y edad se hizo de 
#manera implicita dentro de __ini__

#HERENCIA-----------------------------------------------------------
#Para utilizar herencia utilizamos la funcion super(), que nos permite referirnos al metodo o variables de la clase que heredamos (la clase PADRE)

#CLASE HIJO 
class Alumno(Persona): #Ahora la clase Alumno, recibe todos los metodos y atributos de la clase persona
    def __init__(self,nombre_recibido, apellido_recibido, edad_recibida,curso_recibido,año_recibido):
        #recordar que la clase que hereda los atributos de otra clase su contructor debe recibir los pametros 
        #nesesarios para iniciar las dos clases, la padre y la hijo.
        super().__init__(nombre_recibido, apellido_recibido, edad_recibida) #se inicializa la clase padre y se manda los paramtros necesarios 
        self.curso=curso_recibido #se carga los atributos propio de la clase hijo
        self.año=año_recibido

    def mostrar(self): #Las funciones (metodos) en un clase, no puede tener elementos vacios, como minimo deben tener un seft 
        super().mostrar()
        print("El curso actual es:",self.curso, "y su año de cursado es:", self.año)       


#persona1 = Persona("daniel","bejar", 25)
#persona1.mostrar()

alumno1 = Alumno("daniel","bejar", "26","Curso B","1er Año")
alumno1.mostrar()





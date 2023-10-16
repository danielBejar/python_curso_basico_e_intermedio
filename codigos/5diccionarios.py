#Los diccionarios, son como los que todos conocemos, son conjutos de palabras que estan asociados a un significado, o un valor
#Los diccionarios estan formados por claves (keys) y el valor(values), donde una esta asociada a la otra.
#DATO IMPORTANTE: un diccionario puede tener otros diccionarios dentro suyo.

diccionario={"Nombre del alumno":"Messi", "edad": 31, "carrera": "futbolista"}
print("1------", diccionario)

diccionario_1= dict ([("Nombre del alumno","Escaloni"), ("edad", 38), ("carrera", "tecnico")])
print(diccionario_1)

#Para ver un valor especifico dentro del diccionario 
print("2------", diccionario["edad"]) #muestra el valor asociado a la clave "edad"

#Existe otra forma de buscar un valor es usar del comando get
print("3------",diccionario.get("edad"))

#Para modificar el valor dentro de un diccionario
diccionario["edad"]=35
print("3/1------",diccionario)

#la ventaja de usar el comando get, es que podemos poner un mensaje si no encuentra la clave o el valor que buscamos
print("4------",diccionario.get("altura","No se ha encontrado un valor asociado a esta clave"))

#Tambien podemos buscar claves previamente ingresadas
A="altura"
print("5------",diccionario.get(A,"No se ha encontrado un valor asociado a esta clave")) #Aca le pedimos que busque el str A, dentro del diccionario.

#Los valores de los diccionarios no se pueden repetir
diccionario_2={"Nombre del alumno":"Aguero", "edad": 22, "carrera": "futbolista",  "carrera": "futbolista", }
print("6------",diccionario_2) #Vemos que por mas que se exista dos  "carrera": "futbolista, solamente muestra 1 de ellos


#Se puede sumar valores de un diccionario
edadtotal=diccionario["edad"]+diccionario_2["edad"]
print("7------","La edad total es",edadtotal) #Aca mostraria la edad de ambos  es decir 31+22=44

#Para ver cuantos componentes tiene un diccionario usamos el comando len
print ("8------",len(diccionario)) #Devuele la cantidad de elementos que tiene el diccionario

#Para saber si una clave existe dentro del diccionario usamos el comando in
print("edad" in diccionario) #Retorna un true, si existe la clave "edad" dentro del diccionario.


#Para mostrar TODAS LAS CLAVES de un diccionario , usamos el comando keys
print("10------",diccionario.keys()) #Muestra todas las claves que hay dentro de diccionario

#Para ver todos los valores dentro de un diccionar se usa el comando values.
print("10------",diccionario.values())


#Para agregar un nuevo valor al diccionario
diccionario["Segundo nombre del alumno"]="Leo"
print("11------",diccionario)

#para cambiar un valor dentro del diccionario
diccionario["Nombre del alumno"]="MESSI"
print("12------",diccionario)

#Dentro de un diccionario podemos poner listas, duplas, otros diccionarios, etc

personas={"Nombre":"Fulano", "Notas":[7,8,6], "laboratorios":{"Lab1":"Aprobado", "Lab2":"Desaprovado", "Lab3":"Aprobado" }}
print("13------",personas)

#Se puede reemplazar los valores de un diccionario con los valores de otros
d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2) #reemplaza los valores del diccionario 1 con los valores del diccionario 2
print("14------",d1)


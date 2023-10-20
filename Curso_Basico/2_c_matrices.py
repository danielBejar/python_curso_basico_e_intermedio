V=[[1 ,2, 3, 4], [5,6,7,8]]
print (V) #Imprime toda la matriz en una sola fila
print("-------")

print (V[0]) #Muestra la primera fila de la matriz
print("-------") 


print (V[1])#Muestra la segunda fila de la matriz
print("-------")

for i in range(2): #i va a tomar los valores 0 y 1
         print (V[i])#Muestra la matriz 2x4


print("-------")
print (V[0][0]) #Muesttra el valor 1 , el primer valor de la matriz

print("-------")

for i in range (2):
    for j in range(4): 
         print (V[i][j])#Muestra la matriz en forma de columa
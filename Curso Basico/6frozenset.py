#os frozenset en Python son una estructura de datos muy similar a los set, 
#con la salvedad de que son inmutables, es decir, no pueden ser modificados una vez declarados.


fs = frozenset([1, 2, 3]) #este set ahora no puede ser modificado

#podemos crear un set de frozensets
s1 = frozenset([1, 2])
s2 = frozenset([3, 4])
s3 = {s1, s2} #s3 es un set, no un frozenset y por eso se puede modificar.
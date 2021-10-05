#.array , arange, zeros(()), ones(())
import numpy as np


lista = [1,2,3,4,5,6,7,8,9]
array = np.array(lista)
print(type(array))
lista2 = [["a","b", "c"], [True, False, True]]
array2 = np.array(lista2)
print(array2)
print(type(array2))


array3 = np.arange(6, 20 ,2)
print(array3)
print(type(array3))


matriz_ceros = np.zeros((4,5))
print(matriz_ceros)
matriz_unos = np.ones((3, 5))
print(matriz_unos)


# 40 elementos entre 2 y 6
matriz_linespace = np.linspace(2,6,40)
print(matriz_linespace)

#matriz identidad
matriz_identidad = np.eye(7)
print(matriz_identidad)


#matriz aleatoria, fila, columna
matriz_aleatoria = np.random.rand(3,4)
print(matriz_aleatoria)


#matriz aleatoria, distribucion nommal
matriz_aleatoria_normal = np.random.randn(4)
print(matriz_aleatoria_normal)


#matriz aleatoria enteros
matriz_aleatoria_enteros = np.random.randint(1,51, 200)
print(matriz_aleatoria_enteros)

#reshape

array_aleatoria_enteros2 = np.random.randint(1,100, 54)
array_reshape = array_aleatoria_enteros2.reshape(6, 9)
print(array_aleatoria_enteros2)
print(array_reshape)

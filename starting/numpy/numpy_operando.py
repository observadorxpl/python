import numpy as np;
array = np.random.randint(1, 900, 20)
print(array)
print(f"El valor maximo del array es {array.max()} y su posicion es {array.argmax()}")
print(f"El valor minimo del array es {array.min()} y su posicion es {array.argmin()}")

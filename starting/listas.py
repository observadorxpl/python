#append, extend, remove, index, count, reverse, insert, pop, min, max, sum, len(list), value in list

#remove: remueve el elemento no la posicion*
#index: devuelve la posicion donde se encuentra el elemento
#count: cuenta la cantidad de elementos en la lista
#insert: inserta en una posicion especifica de la lista
#pop: elimina la ultima posicion de la lista

lista = ["Jose", 23, 1997, 2795.3456, True, ["lapiz", "cuaderno", "borrador"]]
for value in lista:
    print(value)
    if(type(value) == list):
        print(value[0])
canales = [4,5,9]
############
print("Seccion 2")
print(lista[:-1000])
print(lista[:9:2])

print(max(canales))
#######
lista.append(False)
lista.append([True, False, "Ok"])
print(lista)

lista.extend(["Laptop", "Monitor", False])
print(lista)
lista.remove(True)
print(lista)
print(lista.index("Laptop"))
print(lista.count(False))
lista.reverse()
print(lista)

#other examples
lista.insert(0, "Pepe")
print(lista)
lista.pop()
print(lista)
print(len(lista))

cuadrados = []
for numero in range(1, 10):
    cuadrados.append(numero * numero)
print(cuadrados)
print(min(cuadrados))
print(max(cuadrados))
print(sum(cuadrados))


#ternary
print("Esta en la lista" if(99 in cuadrados) else "No esta en la lista")    

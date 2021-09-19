#list, map, lambda x: x
lista = [10, 20, 30, 40, 50]
print(list(map(lambda valor: valor* valor, lista)))


#filter
print(list(filter(lambda valor: valor > 20, lista)))

#reduce
import functools
print(str(functools.reduce((lambda valor, next: valor+next), lista)))
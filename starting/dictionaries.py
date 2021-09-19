# dict(...), dict(zip(...)), .items(), .keys(), .values(), .clear()
# items(): retorna la clave y valor pero en tuplas
# clear(): limpiar el diccionario, {}
diccionario = {'nombre': 'Jose', 'apellidos': 'Cayo Acuña', 'tutoriales': ['Python', "Java", "Oracle"]}
print(type(diccionario))
print(diccionario)
print(diccionario['nombre'])
print(diccionario['tutoriales'][:3])

for clave in diccionario:
    print(f"clave: {clave}, valor: {diccionario[clave]}")
    
persona = dict(nombre = "Jose", apellido = "Cayo Acuña", edad =23)
print(type(persona))

diccionario02 = dict(zip('aeiou', [1,2,3,4,5]))
print(diccionario02)
print(type(diccionario02))
print(diccionario02.items())
print(diccionario02.keys())
print(diccionario02.values())

diccionario02.clear()
print(diccionario02)
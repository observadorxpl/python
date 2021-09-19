print(type(38))
print(type(23.3))
print(type('Ok'))
print(type(True))
print(type(False))
# comentarios
print("Hola, "+ "Amigos")
print("Jose"*4)
variable = "Cadena en variable,"
variable += "fin."
print(variable)
print(variable[-23]) #C
print(variable[0:5]) 
print(variable[-5:5]) 
print(len(variable)) 
print(variable.upper()) 
print(variable.lower())
print(variable.capitalize())

variable_con_espacios= "               Cadena               con              espacios              .              "
print(variable_con_espacios.strip()) #solo al inicio y al final

#replace
print(variable_con_espacios.replace(" ", ""))
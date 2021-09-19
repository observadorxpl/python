# Las tuplas son inmutables
# tuplas unitarias (value, ), sino sera de tipo primitivo, es necesario la coma
# empaquetado y desempaquetado de tuplas
colores = ("verde", "amarrillo", "rojo", "azul")
print(type(colores))
print(colores[:2])

tupla = ()
print(type(tupla))
#colores [2] = "valor" # error, es inmutable
print(len(colores))

tupla_unitaria = (50,)
print(type(tupla_unitaria))


#empaquetado
a = 10
b= 290.44
c= "Jose"
tupla_empaquetado = a, b, c
print(type(tupla_empaquetado))

#desempaquetado
a, b , c= tupla_empaquetado
print(a)
print(b)
print(c)
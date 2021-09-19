#startswith, endswith, center, ljust, rjust, len
texto = "51927377402"
print(texto.startswith("51"))
print(texto.endswith("402"))



#alinear texto
texto = "Esto es un texto para de ejemplo."
print(texto.center(80, '+'))
print(texto.center(80, '-'))
print(texto.center(35, '-'))
print(len(texto))


#izquierda (del texto)
print(texto.ljust(80, '-'))
print(texto.rjust(80, '-'))

#eliminar espacios en blanco
texto = "Cadena con      es pa  ci o s en b l an  cos y c a r a cte res ex tr a ños *_==)'=()/(%&&#\\!"
print(texto.strip()) # solo al inicio y final de la cadena
print(texto.replace(" ", "")) # solo al inicio y final de la cadena
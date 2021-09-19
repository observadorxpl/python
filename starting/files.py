#guardar datos en archivos
escritura = open("archivo.txt", "w")
escritura.write("Esto se escribe en el archivo \ny esto es una linea siguiente \n\t\t\tY esto es otra linea tabulada")
escritura.close()

#lectura de fichero
lectura = open("archivo.txt", "r")
print("---------")
#print(lectura.readline()) # solo una linea
print("---------") 
#print(lectura.read())# lee todo
lista_lineas = lectura.readlines()
for linea in lista_lineas:
    print(linea)
lectura.close()
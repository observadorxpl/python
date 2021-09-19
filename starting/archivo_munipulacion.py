import os;

#mostrar directorio actual
print(os.getcwd())


#crear carpeta o directorios
os.makedirs("Micarpeta")
#listar contenido
print(os.listdir("./"))

#mostrar tamaño de carpeta o directorio
print(os.path.getsize("MiCarpeta"))

#comprobar si es archivo o carpeta
print(os.path.isfile("MiCarpeta"))
print(os.path.isdir("MiCarpeta"))

#cambiar directorio
os.chdir("MiCarpeta")
print(os.getcwd())
print(os.listdir("./"))
os.chdir("../")
print(os.getcwd())

#renombrar carpeta
os.rename("MiCarpeta", "NuevaCarpeta")

#borrar archivos
os.remove(os.getcwd()+"/archivo.txt")
print(os.listdir("./"))

os.rmdir("NuevaCarpeta")
os.chdir("../")
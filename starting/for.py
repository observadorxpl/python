#for x in range(y,z). z no incluide. can you use range(x)
#tabla de multiplicar (for)
tabla = int(input("Que tabla de multiplicar quieres?:"))
hasta = int(input("Hasta que numero lo quieres?:"))
for count in range(1, hasta+1):
    print(f"{tabla} x {count} = {tabla*count}")


#for list
nombres = ["Jose", "Marcos", "Pepe", "Javi"]
for nombre in nombres:
    print(nombre.upper())
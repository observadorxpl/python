#while, break
#tabla de multiplicar
tabla = int(input("Que tabla de multiplicar quieres?:"))
hasta = int(input("Hasta que numero lo quieres?:"))

count = 1
while(count <= hasta):
    print(f"{tabla} x {count} = {tabla*count}")
    count+=1
    if count>12: break
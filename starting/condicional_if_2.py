#####################
edad= float(input("Dime tu edad y te dire tu tarifa:"))

if(edad < 5):
    precio = 0
elif (edad < 15):
    precio = 5
elif (edad < 65):
    precio = 20
else:
    precio = 15
print(f"Tu tarifa para entrar es de S/.{precio}")
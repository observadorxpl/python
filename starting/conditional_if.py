#if elif else
# <>, <=, >=, !=, ==, not, and, or
# pass
print(not 3>5) #True

#####################
num_one= float(input("Insert firts number: "))
num_two= float(input("Insert second number: "))

if(num_one>num_two):
    print(f"El numero mayor es: {num_one}")
    #pass
elif (num_one < num_two):
    print(f"El numero mayor es: {num_two}")
else:
    print(f"Los dos numeros son iguales")
    

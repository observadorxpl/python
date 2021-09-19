def operar(option_selected, number_one, number_two):
    if(option_selected == "1"):
        return sumar(number_one, number_two);
    elif(option_selected == "2"):
        return restar(number_one, number_two)
    elif(option_selected == "3"):
        return multiplicar(number_one, number_two)
    elif(option_selected == "4"):
        return dividir(number_one, number_two)
    else:
        return 0
        
def sumar(number_one, number_two):
    return number_one+number_two;

def restar(number_one, number_two):
    return number_one-number_two;

def multiplicar(number_one, number_two):
    return number_one*number_two;

def dividir(number_one, number_two):
    return number_one/number_two;


print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
option_selected = ""


while(option_selected not in {"1","2", "3", "4", "5"}):
    option_selected = input("Selecciona una opcion: ")
    if(option_selected == "5"):
        break
if(option_selected != "5"):
    number_one=float(input("Ingrese el primer numero: "))
    number_two=float(input("Ingrese el segundo numero: "))   
    result = operar(option_selected, number_one, number_two);
    print(f"El resultado de la operación es: {result}")


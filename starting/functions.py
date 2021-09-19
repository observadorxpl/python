def isPair(number):
    return "El numero es par" if (number%2 == 0) else "El numero es impar"

number = float(input("Insert the number to evaluate: "))
print(isPair(number))


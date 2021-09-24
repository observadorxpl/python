numero_uno = 45
numero_dos = 0

import os;
try:
    print(numero_uno / numero_dos)
except:
    print("Error controlado")
finally:
    print("Culmino la validacion try except")

#print(os.getcwd()+"/archivo454.txt")    
try:
    os.remove(os.getcwd()+"/archivo454.txt")
except FileNotFoundError:
    print("Error controlado, no se ha podido encontrar el archivo")
except ZeroDivisionError:
    print("Error controlado, no se puede dividir un numero por 0")
finally:
    print("Finaliza ejecucion try except")
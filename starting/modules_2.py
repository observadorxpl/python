#importamos la funcion randit del modulo random, y le damos un alias
from random import randint as azar
#no recomendable
#from random import *
#import random
continua = "s"
while(continua == "s" or continua == "S"):
    lanza_dado = azar(1,6)
    print(f"Has sacado un {lanza_dado}")
    continua = input("Continuamos(s/n): ")
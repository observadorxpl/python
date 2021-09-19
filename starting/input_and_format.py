from datetime import datetime;
from datetime import timedelta;
DIAS_X_ANIO=365
nombre = input("Cuál tu nombre:")
edad = int(input("Cuál es tu edad:"))
now = datetime.now()

print(f"{nombre}, naciste en: {now - timedelta(days=edad*365)}")
#print(f"{nombre} tu fecha de nacimiento fué el )

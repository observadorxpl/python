#pass si en caso no definimos metodos o atributo para la clase; vacia.
class Vehiculo:
    def __init__(self, color, marca, encendido = False) -> None:
        self.color = color
        self.velocidad = 0
        self.marca = marca
        self.encencido = encendido
    #pass
    def arrancar(self):
        if not self.encencido:
            self.encencido = True
    
    def acelerar(self):
        if self.encencido:
            self.velocidad+=10
            print(f"Acelerando a velocidad: {self.velocidad}")
        else:
            print(f"El vehiculo no está encendido: {self.encencido}")
    
    def frenar(self):
        if self.encencido and self.velocidad > 10:
            self.velocidad -=10
        else:
            self.velocidad = 0
        print(f"frenando a velocidad: {self.velocidad}")
        
    def mostrar_estado(self):
        print(f"Soy de la marca {self.marca}, con un color {self.color} y mi velocidad actual es {self.velocidad}")


class Coche(Vehiculo):
    def __init__(self, color, marca, ruedas, encendido=False):
        super().__init__(color, marca, encendido=encendido)
        self.ruedas = ruedas
    def mostrar_estado(self):
        print(f"Soy de la marca {self.marca}, con un color {self.color} y tengo {self.ruedas} ruedas.")
#Instanciar un objeto

peugeot = Coche('rojo', 'Peougeot', 2)
renault = Coche('verde', 'Renault', 3)

renault.mostrar_estado;

peugeot.arrancar()
peugeot.acelerar()
peugeot.acelerar()
peugeot.acelerar()
peugeot.acelerar()
peugeot.acelerar()
peugeot.acelerar()
peugeot.frenar()
peugeot.frenar()
peugeot.frenar()
peugeot.frenar()
peugeot.mostrar_estado()




#renault.arrancar()
renault.acelerar()
renault.frenar()
renault.mostrar_estado()
print(peugeot)
print(type(peugeot))
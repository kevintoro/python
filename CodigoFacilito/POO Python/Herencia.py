#Vamos a ver cómo maneja python las herencias de clase
class Animal:

    def comer(self):
        print("Comiendo...")

    def dormir(self):
        print("Durmiendo...")

    def comun(self):
        print("es un método de animal")

class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha = fecha

    def obtener_fecha(self):
        print(self.fecha)

    def comun(self):
        print("es un método de mascota")


#Para hacer herencia, pasamos como parámetro la clase padre, a la clase hijo
class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Woff...")

    def dormir(self):
        print(self.nombre, "está durmiendo")
        #esto es opcional:
        Animal.dormir(self)
        print("No molestar...")

    '''
    def comun(self):
        print("es un método de perro")
    '''
firulais = Perro("firulais")
firulais.comer()
firulais.ladrar()
firulais.dormir()
firulais.fecha_adopcion("07-07-2018")
firulais.obtener_fecha()
firulais.comun()
"""
    puede haber un método con el mismo nombre, hasta en la clase hijo, si es el caso, entonces tomará el método del hijo
    si no, entonces mira el orden de los padres, de izquierda a derecha
"""

#Podemos hacer sobrescritura de métodos, todo:mirarlo en la clase perro
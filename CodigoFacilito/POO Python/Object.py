'''
    Toda clase, aunque no se lo pasemos entre paréntesis, hereda de la clase Object, y eso lo vemos con los métodos que
    podemos modificar que los identificamos con "__" al principio y al final, tal como lo es init (que no es un constructor)
    ello lo veremos luego...
'''

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "ésto es un gato, llamado {}".format(self.nombre)

class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "ésto es un pato, llamado {}".format(self.nombre)


pato = Pato("Lukas")
gato = Gato("Tom")

print(pato)
print(gato)

#Así sabremos los atributos de un objeto:
print(pato.__dict__)
print(gato.__dict__)
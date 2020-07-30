#aquí hablamos de métodos estáticos:
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @staticmethod
    def area(base, altura):
        return (base*altura)/2

print(Triangulo.area(10,20))

"""
    Con los métodos estáticos no se puede usar variables de instancia, tienen que ser pasados todos por parámetros
    tal como lo vemos en el ejemplo anterior, sin embargo, sí podemos usar variables de clase y ello funcionará correctamente
"""

#ahora veremos, "métodos de clase", usamos por convenienca "cls"

class Circulo:
    pi = 3.14159265

    @classmethod
    def area(cls, radio):
        return cls.pi*radio**2

res = Circulo.area(10)
print(res)


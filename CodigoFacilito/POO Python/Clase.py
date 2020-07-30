#esta es la manera de crear una clase, hay que tener en cuenta que la primera letra es Mayúscula
"""ésta es una clase que nos va a crear usuarios con diferentes atributos"""
class Usuario:
    """
        Init nos permite definir los atributos del objeto, algo así como un constructor, claro que
        son variables que son para cada instancia.

        Para definir las variables de clase (que se van a repetir para cada uno de los objetos el mismo dato),
        se deben colocar afuera y con su valor de inicialización..
    """
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def presentacion(self):
        return "¡Hola!, mi nombre es {}, mi username {}, y mi correo es {}".format(self.name, self.username, self.email)

kv = Usuario("kv","Kevin Toro", "kevinandrestg7@gmail.com")
print(kv.presentacion())

class Circulo:
    pi = 3.14159265

    def __init__(self, radio):
        self.radio = radio

    def obtener_area(self):
        return  (self.pi*(self.radio*self.radio))

c1 = Circulo(25)
print(c1.obtener_area())
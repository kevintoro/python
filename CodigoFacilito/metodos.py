def saluda(nombre):
    print('hola {}, espero que estés bien..'.format(nombre))

def suma(a, b):
    if type(a) != str and type(b) != str:
        return a+b
    else:
        return 'No se pueden sumar los valores dados en entrada'

#podemos returnar diferentes valores:
def curso_actual():
    return "curso de", "Python", 3

saluda("Kevin Toro")
print(suma(15.6, "87"))

inicio, curso, numero = curso_actual()
print("{} {} {}".format(inicio, curso, numero))

#funcion que retorna un diccionario:
"""
    Nosotros podemos colocar valores por deffault con un "=" en los argumentos, como por ejemplo:
    def devolver(nombre, apellido, edad=10) -> valor por defecto para edad = 10, por si el usuario se salta
    el colocar el valor que va ahí y evitar los errores, 
"""
def devolver_diccionario(nombre='', apellido='', edad=10):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{} {}".format(nombre, apellido),
        'edad': edad
    }

kevin = devolver_diccionario("kevin", "toro", 20)
print(kevin)
#PODEMOS COLOCAR EL NOMBRE DEL PARAMETRO PARA REFERIRNOS A ALGÚN PARAMETRO kv = metodo(apellido="Toro")

#Podemos hacer que pida una infinidad de datos puestos por el usuario, eso se llama args y va con un *, veamos:
def sumar_numeros(*args):
    total = 0
    for valor in args:
        if type(valor) == str:
            print(valor)
        else:
            total += valor
    return total

print(sumar_numeros("Hola Mundo", 5, 7, 8.9, 7.6))

#también se pueden colocar parámetros obligatorios junto con los "args"
def familia(apellido_familia, *args):
    temp = "Familia: {}, integrada por".format(apellido_familia)
    integrantes = []
    integrantes.append(temp)
    for nombre in args:
        integrantes.append(nombre)
    return integrantes

print(familia("Toro Galván", "Olivo Toro", "Luz Galván", "Kevin Toro", "Janner Toro", "Daiver Toro"))

#Esta es otra forma de hacer el multi parámetros: por conveniencia se llamara **kwargs, esto generará un Diccionario
def lista_tareas(**kwargs):
    print(kwargs)

lista_tareas(nombre="kevin", apellido="toro", casado=False, edad=20)

'''
    Para referirnos a una variable que es Global, dentro de un metodo, y que su valor para lo demás del script se 
    modifique, es necesario en la función usar la palabra reservada "global" junto con la variable a la que nos vamos
    a referir en ese Script, veamos un ejemplo:
'''
animal = "Perro"
def cambio_de_animal(nanimal):
    global animal
    animal = nanimal

cambio_de_animal("Toro")
print(animal)

#Veamos acerca de funciones lambda o funciones anónimas:

grados = lambda celcius = 0: (celcius*(9/5))+32
print(grados(20))

#Función map, nos permite ejecutar una función con un objeto iterable, y luego volverlo una lista, o tupla

def cuadrado(numero):
    return numero*numero

listadonum = [2,3,4,5]
resultado = map(cuadrado, listadonum) #hay que tener en cuenta que la función no debe tener paréntesis para evitar error
new_list = list(resultado)

print(new_list)

listadonum.append(6)
#También se puede colocar una expresión lambda dentro de map
res = map(lambda numero: numero*numero, listadonum)
new_list = list(res)
print(new_list)

'''
    Las funciones pueden estar también anidadas, teniendo en cuenta de que esa función dentro de la otra, sólo puede 
    ser llamada ahí, y debe ser llamado en esa función:
'''
def funcion_nueva(lista):
    def otra_funcion():
        nonlocal lista
        lista = ['esto', 'es', 'otra', 'lista']
        print(lista)
    otra_funcion()

lista = ['esta','es','la','lista','main']
funcion_nueva(lista)
print(lista)

def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1,maximo+1):
        yield numero*posicion, numero, posicion

for res, numero, posicion in tabla_multiplicar(9):
    print("{} x {} = {}".format(res, numero, posicion))
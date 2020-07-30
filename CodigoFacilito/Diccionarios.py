#Un diccionario se puede definir de las siguientes maneras:
dicc1 = {}
dicc2 = dict()
'''
    siempre debe llevar una llave y un valor, además, se pueden modificar, agregar items, etc
    se parece mucho al manejo de archivos JSON, además de que podemos usar clases como llaves
'''

dicc1["nombre"] = "Kevin Toro" #Así agregamos una llave con su valor
print(dicc1)
print(dicc1["nombre"])#Así obtenemos elementos, dada la llave

'''
    No pueden existir llaves duplicadas, en caso de eso, tomará el último valor asignado
    en caso de que no se encuentre la llave dentro del diccionario, nos dará un error,
    podemos saber si una llave se encuentra en el diccionario, de la siguiente manera:
'''

print("nombre" in dicc1)

'''
    Uso de método get:
    si colocamos una llave que existe, nos dará el valor que tenga, si no, sólo devolverá 'None'.
    También le podemos decir que devuelva un valor de cualquier tipo de dato para cuando no consiga la llave
    dicc1.get("edad", "no se encuentra")
    
    Métod setdefault:
    
    si colocamos llave que existe, nos devuelve el valor, en caso de que no exista, esta llave se agregará al
    diccionario siendo el primer elemento la llave, y el segundo el valor
    
    dicc1.setdefault("z", {}) -> se agregaría un valor z con un diccionario vacío.
'''

print(dicc1.keys())
#También podemos mostrarlas como si fuera una lista:
print(tuple(dicc1.keys()))
#Así podemos mostrar los valores que hay en el diccionario:
print(dicc1.values()) #También podemos mostrarlo con el método tuple()
#y de la siguiente manera podemos obtener todos los items del diccionario
print(dicc1.items())
#o mostrarlo como lista o tupla:
print(list(dicc1.items()))

dicc2 = {'a':1, 'b':2, 'c':3, 'd':4}
print(dicc2)

#Eliminar un item del diccionario, llave y valor, con lo siguiente:
del dicc1["nombre"];
#Otra manera es usando el método de diccionarios 'pop'
dicc2.pop('a')
print(dicc2)

#para eliminar todos los item, puedo usar diccionario = {}, o como las listas: diccionarios.clear()
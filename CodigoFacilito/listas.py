lista = ["Python", "DJango", "Flask", "C", "C++", "C#", "Java", "PHP"]
print(lista.__len__())
print(lista[0])

#se pueden obtener sublistas :o

sub = lista[0:3]
print(sub)
sub = lista[:3] #Python entenderá que va desde el indice 0
print(sub)
sub = lista[3:] #Python entiende que quiero todo el listado desde x hasta lenght
print(sub)
sub = lista[0::2] #Con saltos de 2 en 2
print(sub)
sub = lista[::-1] #Invertir la lista :u
print(sub)

#Ordenamiento de los objetos que hay dentro de una lista:
num = [5, 9, 4, 5, 7, 6, 14, 5.5, 4.1 ,2.6, 8, 1]
print(num)
num.sort(reverse = True)
print(num)
num.sort()
print(num)
num_mayor = max(num)
num_menor = min(num)
print(num_menor, num_mayor)

longitud = len(num)
print(longitud)

#saber si un número está en la lista:
res = 5 in num
print(res, 'Índice [',num.index(5),'], Está:', num.count(5), 'veces')

#ahora vamos a trabajar con matrices, los puedo crear a partir de dos listas
lista1 = [10,20]
lista2 = [5,4]

matriz = [lista1, lista2]
print(matriz[0][0])

"""
    Las tuplas son una estructura de datos como las listas, sólo que, no pueden ser modificadas, una vez se definen
    se quedaran así el resto del programa, es muy útil para cuando queremos manejar valores constantes en todo
    nuestro programa..
    
    tupla = (), nombre de la variable, igual a, paréntesis, los datos se deben separar por una coma
    
    las tuplas son más rápidas para obtener elementos, se trabajan con los índices, así como se hace con las listas
"""

tupla = (1,2,3,4,5,6,7,8,9)
print(tupla[4]) #se pueden hacer los mismos procesos que con las listas, usando los [::]

#Observemos el siguiente comportamiento de la tupla y variables
uno, dos, tres, cuatro, *cinco = tupla
print(uno, dos, tres, cuatro, cinco) #El * convierte en una lista la última variable, Python sabe asignar a variables
nueva_lista = [10,20,30,40]
nueva_tupla = (100,200,300,400)
result = 20 in nueva_lista
print(result)

#La función zip, devuelve un objeto del tipo zip
result = zip(tupla, nueva_lista, nueva_tupla)
print(result) #No da información de lo que hay dentro del objeto
result = tuple(result)
nueva_lista = list(result)
print(result, nueva_lista)

#de lista a tupla
nlista = ["Curso", "Python", "CodigoFacilito"]
ntupla = ("Introducción", "Básico", "Listas", "Tuplas")

#tupla a lista:
varlist = list(ntupla)
print(varlist)
#lista a tupla:
vartup = tuple(nlista)
print(vartup)

#los strings pueden pasar a ser lista o tupla
mensaje = "Este es el curso de Python"
varlist = list(mensaje)
vartup = tuple(mensaje)
print(varlist, "\n", vartup)

'''
    El None, es para tener una variable sin que tenga algo (aunque python puede tomarlo como un valor False)
    los valores que sean vacíos o nulos, tomaran valor para Python como false, en este caso con el None, también pasará ello
'''

color_show = 'rojo'

if color_show == 'verde':
    print('Puede continuar')
elif color_show == 'amarillo':
    print('preparados...')
else:
    print('Detenerse')

#Ciclo While, funciona igual que Java, aunque después del ciclo, podemos usar la operación booleana 'else'
# haremos un algoritmo que nos permita saber cuántos dígitos tiene un número

numero = 123456789
cont = 0

while numero >= 1:
    numero = numero/10
    cont+=1
else:
    print('Entró aquí')

print(cont)

numero = 0

'''
    En el caso del for, hay que tener en cuenta que trabaja sólo con objetos que pueden ser iterables, tales como las listas []
    las tuplas() y los diccionarios{}, veamos un ejemplo, la estructura es:
    
    for variablex in objeto_iterable:
        codigo a ejecutar..
'''

numeros = [1,2,3,4,5,6,7,8,9]

for numero in numeros:
    print(numero)

#Cuando recorremos un diccionario, lo que vamos a ver son los diccionarios, y no los valores..
#Veamos el siguiente ejemplo usando más tipos de estructura de datos:

values = ((10,20),["String", "string"],(True, False))

for valor in values:
    print(valor)

#Pero en el for puedo colocar otra variable para visualizar dentro de las estructuras
#todo: hay que tener en cuenta que las variables deben ir con la cantidad de valores que hay dentro de las estructuras de datos
for valor, inside in values:
    print(valor, inside) #Veremos los valores sin el tipo de estructura

#Secuencia range, es para movernos en una secuencia de números..

for nums in range(10):
    print(nums)

#Pero si quiero colocar un número de comienzo y que termine dónde (el último número no se tiene en cuenta) le digo, es así:
for nums in range(1,10):
    print(nums)

#También se pueden colocar números negativos:
for nums in range(-10,11):
    print(nums)

#Incluso pedir que sea de 2 en 2:
for nums in range(1,21,2):
    print(nums)

#range puede tener también un len
lista = [1,2,3,4,5,6]
for nums in range(len(lista)):
    print('índice:',nums, ', valor:', lista[nums])

lista.clear()
lista = [9,8,7,3,2,1]

#Ahora enumerate:
for indice, valor in enumerate(lista):
    print('índice:',nums, ', valor:', lista[nums])

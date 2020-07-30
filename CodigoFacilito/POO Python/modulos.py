import calculadora

res = calculadora.suma(1,2,3,4,5,6)
print(res)
print(calculadora.resta(7,1,2,3))
print(calculadora.multiplicacion(7,2,2))

'''
    También podemos importar usando:
    from calculadora import *
'''

from calculadora import *

print(suma(65,40,60))

#En el import se puede colocar todos los elementos necesarios separando por ","
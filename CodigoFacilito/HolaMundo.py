print('Hola Mundo xD')
existe = False 
tutor = 'Kevin'

if existe:
    print('Sí Existe')
else:
    print('No Existe')

if tutor.__eq__('Kevin Toro'):
    print('Tutor es Kv')
else:
    print('Kelly perokhemondá')

# Se pueden asignar a varias variables valores distintos en la misma línea:
valor1, valor2, valor3 = 'Kevin', False, 10*5
print('los valores de las variables son: '+valor1, valor2, valor3)

#Operadores lógicos justo como Java, pero los diferencia los and, or, not
result = True and tutor.__eq__('Kevin'); #Todos deben ser verdaderos para dar resultado verdadero
print(result)
result = True or existe #deben ser almenos 1 verdadero
print(result)
result = not True #cambia el valor que haya en el boolean
#dos enteros se pueden comparar con la palabra reservada 'is'
numx = 10 
numz=10

result = numx is numz
print(result)
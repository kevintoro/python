"""
    Serie de ejercios que se han dejado en el curso de Python de Código facilito
    para seguir practicando, todo debe estar legible
"""

#Ejercicio de hallar el área de un triángulo
base = int(input('Base del triángulo: '))
altura = int(input('Altura del triángulo: '))
res = (base*altura)/2
print('Área del triángulo dado: ',res)

#Ejercicio de pasar USD a COP
usd = float(input('Cantidad de USD: '))
res = 3827.5 * usd
print(usd, 'USD = ',res,'COP')

#Ejercicio de pasar °C a °F
celcius = float(input('Cantidad de grados a convertir: '))
res = (celcius*(9/5)+32)
print(celcius, '°C es igual a: ', res, '°F')

#Calcular cantidad de segundos en un lustro
day = 3600*24
print(day)
year = 365*day
print(year)
lust = year*5
print('Un lustro o 5 años equivale a: ', lust, 'Segundos')

#Hallar tiempo que tarda la luz para llegar del sol a marte
sol_marte = 227940000
velocidad_luz = 300000
res = sol_marte/velocidad_luz
min = res/60
print('La distancia del sol a marte es: ', sol_marte,'\nLa velocidad de la luz es: ', velocidad_luz, 
'\nLa luz desde el sol a marte tarda:', res, 'segundos, o, ', min, 'minutos')

#Hallar la cantidad de vueltas que da una rueda de x diámetro en k kilómetros
import math

km = float(input('Kilometros recorridos: '))
diam = float(input('Diámetro de rueda (cm): '))
circunferencia = (math.pi*diam)
circunferencia_metros = circunferencia/100
print('Circunferencia(cm) = ', circunferencia)
print('Circunferencia(mts) = ', circunferencia_metros)
res = ((km*1000)/circunferencia_metros)
print('En', km, 'Km, una rueda con diámetro igual a', diam, 'la rueda da',res, 'vueltas')

#Validar si dos edades son iguales 
edad_usuario1 = int(input('Edad: '))
edad_usuario2 = int(input('Edad: '))
print(edad_usuario1==edad_usuario2)

#Calcular cuántos meses han pasado desde el nacimiento de una persona
from datetime import date
from datetime import datetime

present = date.today()
day = int(input('Día de nacimiento: '))
month = int(input('Mes de nacimiento: '))
year = int(input('Año de nacimiento: '))
birth = date(year, month, day)
dif = present - birth
only_days = dif.days
years = only_days/365
months = years*12
print('La cantidad de meses entre la fecha de su nacimiento y la actual es:',months)


#Hallar promedio dadas 5 notas:
esp = float(input('Nota de Español: '))
math = float(input('Nota de Matemáticas: '))
econ = float(input('Nota de Economía: '))
prog = float(input('Nota de Programación: '))
ing = float(input('Nota de Inglés: '))

prom = (esp+math+econ+prog+ing)/5
print('El promedio entre todas las materias es:',prom)
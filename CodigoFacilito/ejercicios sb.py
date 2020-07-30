"""
#1. Promedio entre materias:
calificaciones = {'calculo':8, 'programacion':9, 'dibujo':5}
res = 0
for calf in calificaciones:
    res += calificaciones.get(calf)

res /= len(calificaciones)
print('Promedio de calificaciones:',res)

#2. Materia con mejor calificación:
print(max(calificaciones.values()))

#3. Lista que guarda 10 números positivos ingresados por el usuario, halla el mayor, el menor, y el promedio entre ellos
numeros = []
for num in range(1,11):
    numeros.append(int(input('{}. Ingrese un número entero:'.format(num))))

res = 0
for num in numeros:
    res+=num

res /= len(numeros)
numeros.sort(reverse=True)
print('Número mayor: {}, número menor: {}, promedio de suma: {}'.format(numeros[0], numeros[-1], res))


palabras = []
cant = int(input('¿Cúantas palabras desea ingresar?: '))
val = 1
while(val <= cant):
    palabras.append(input('Palabra #{}: '.format(val)))
    val+=1

for palabra in palabras:
    sub = palabra[::-1]
    if sub == palabra:
        print('Palíndrome:', palabra)
"""

#4 Encontrar la palabra que más se repite, y ver cuántas veces lo hace.
parrafo = '''El próximo domingo, los ciudadanos tendrán ocasión de hacer política, de participar en la toma
de decisiones públicas, cuando depositen su voto para elegir a 194 diputados de mayoría y tal vez cincuenta de partido.
La democracia electoral les permite, de ese modo ejercer  funciones de gobierno.

Pero ¿de verdad es así? La respuesta tiene que ser negativa. La política no se hace en las urnas.
El sistema de partido hegemónico que impera en México desde 1929 determina que la verdadera elección de diputados
haya ocurrido en febrero, probablemente cuando los diversos intereses que es aglutinan en el PRI acordaron las candidaturas,
en un proceso que sólo es formalmente la interior, pero que por la naturaleza del partido es el que verdaderamente decide
la composición de la Cámara.

Apenas dieron las 6 de la mañana, despuntaba el sol, e iluminaba la población, mostrando lo que la oscuridad de la
noche no había dejado ver a mi arribo: varias casas con tejas esmaltadas, brillando bajo los primeros rayos del sol;
la sombra de la torre de la iglesia pasando por el centro de la plaza hasta terminar con la sombra de la cruz sobre
la puerta del palacio municipal. A un lado, los comercios del mercado que han abierto antes del alba: la carnicería,
la recaudería, con verduras recién cortadas, en la tienda de abarrotes, frijol y maíz de la última cosecha…
Después de 40 años, ese amanecer me llenó el corazón.
'''

parrafo = parrafo.lower()
parrafo = parrafo.split()
repetidas = []

for palabra in parrafo:
    repetidas.append(parrafo.count(palabra))

most = max(repetidas)
index = repetidas.index(most)
print('Palabra más repetida es: {}, con una cantidad de: {}'.format(parrafo[index], most))

#5. Pedir una frase dada por el usuario, y ver letra por letra dónde se encuentra en el abecedario
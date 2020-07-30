curso = "Curso de Python 3"
print(len(curso)) #Aquí obtengo el tamaño del String
#Puedo manejar los Strings como si fueran una lista o una tupla
print(curso[0:len(curso):2])
tam = curso.index("so")
print(tam)
#Los strings no se pueden modificar, tal como pasa con las tuplas

lenguajes = "Python; Java; Ruby; PHP; Swift; Javascript; C#; C; C++"
res = lenguajes.split() #Retorna una lista a partir de un texto que hemos utilizado (separador por defecto es " ")
print(res)
#También podemos personalizar el separador
res = lenguajes.split(";")
print(res)
#Se puede ser más específico como el siguiente caso:
res = lenguajes.split("; ")
print(res) #Vemos los lenguajes sin espacios, y sin ";"
separador = "; "
nuevostr = separador.join(res)
print(nuevostr)

saltos_linea = """Este es un texto
con saltos
de
línea"""

res = saltos_linea.splitlines()
print(res)

#Formato de Strings
print(curso.capitalize()) #pone la primera letra en mayúscula, y el resto en minúscula
print(curso.swapcase()) #Invierte de mayúsculas a minúsculas o viceversa
print(curso.upper()) #Todas las letras a mayúsculas
print(curso.lower()) #Todas las letras a minúsculas
print(curso.isupper(), curso.islower()) #pregunta si todas las letras son mayúsculas o minúsculas
print(curso.title()) #Pone el texto en formato de título, las primera letra de cada palabra en mayúscula

#Reemplazo de algunas palabras dentro de una cadena de texto
res = curso.replace("Python", "Ruby")
#el replace también puede pedir la cantidad de veces que queremos que sea reemplazada la palabra
curso = "Curso de Python, Python básico"
print(curso.replace("Python", "Ruby", 1))

#Quitar espacios que se pueden encontrar al principio o al final del texto original
nuevo_string = " Hola Mundo "
print(nuevo_string.strip()) #Veremos que ya no aparecen espacios en el texto

#Agregando strings de variables a un string existente (formato)
curso = "Curso"
name = "Python"
nuevo_string = "Este es un %s de %s" %(curso, name)
print(nuevo_string)

#También podemos hacer lo mismo, con el método format, pero usando llaves ({})
nuevo_string = "Este es un {} de {}".format(curso, name)
print(nuevo_string)
#También podemos hacerlo así:
nuevo_string = "Este es un {a} de {b}".format(a = curso, b = name)
print(nuevo_string)
#Hay que tener en cuenta que al darle nombre a las asignaciones, lo puedo colocar en cualquier lado de la expresión:
nuevo_string = "Este es un {a} de {b}, a decir verdad me está encantando {b}".format(a = curso, b = name)
print(nuevo_string)

#Tema de concatenación de Strings
curso = "Curso de Python"
#vamos a cambiar la "C" por una "c"
curso = "c"+curso[1:]
print('nueva salida:',curso) #Si uso la coma, siempre va a dejar un espacio, pero si coloco un "+" no
#todo: para los tipos de datos que no son String, nos podemos apoyar de la función str()

#SABER SI UN STRING ESTÁ DENTRO DE OTRA:

texto = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"
if texto.count("nanana") > 0:
    print(True, ', Está', texto.count("e"), 'veces')
else:
    print(False)

#Otra manera es hacerlo con el método .find("")
substring = "texto un grande"
res = texto.find(substring)
if res != -1:
    print(texto[res:(res + len(substring))])
else:
    print('Valor no encontrado en el texto')

'''
    También puedo comentar varias líneas con las triples comillas simples UwU
'''

persona1 = ["Kevin Toro", 20, "Colombia"]
persona2 = ["Marggie Garcia", 21, "Colombia"]
persona3 = ["Allison Toro García", 10, "USA"]

listado_personal = [persona1, persona2]

if persona3 in listado_personal:
    print('Encontrado en la lista')
else:
    print('No se encontró en la lista')
    listado_personal.append(persona3)
    print('Persona agregada')

print(persona3 in listado_personal)

x = 0
while x < 3:
    y = 0
    while y < 3:
        if str(listado_personal[x][y]).__contains__("Allison"):
            print('Valor encontrado')
            break
        y = y+1
    x = x+1

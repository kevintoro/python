def resta(*args):
    total = args[0]
    nlist = args[1:len(args)]
    for valor in nlist:
        if type(valor) is str:
            print("valor '{}' no es numérico, se ignorará".format(valor))
        else:
            total -= valor
    return total

def suma(*args):
    total = 0
    for valor in args:
        if type(valor) is str:
            print("valor '{}' no es numérico, se ignorará".format(valor))
        else:
            total+=valor
    return total

def multiplicacion(*args):
    total = args[0]
    nlist = args[1:len(args)]
    for valor in nlist:
        if type(valor) is str:
            print("valor '{}' no es numérico, se ignorará".format(valor))
        else:
            total *= valor
    return total

def division(dividendo=1, divisor=1):
    return dividendo/divisor
'''def imprimir(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    imprimir(maximo, atual + 1)


imprimir(10, 1)'''


def imprimir(maximo, atual):
    if atual < maximo:
        print(atual)
        imprimir(maximo, atual + 1)


imprimir(900, 1)

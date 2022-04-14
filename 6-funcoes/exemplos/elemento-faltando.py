def elemento_faltando(lista1, lista2):
    for i in lista2:
        esta = False
        for j in lista1:
            if i == j:
                esta = True
        if not esta:
            elemento = i
            break
    return elemento


lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 4, 5]

assert elemento_faltando(lista1, lista2) == 5
assert lista1 == [1, 2, 3, 4]
assert lista2 == [1, 2, 3, 4, 5]

def meu_in(lista, elemento):
    for e in lista:
        if e != elemento:
            return False
    return True


def meu_max(lista):
    maximo = None
    for num in lista:
        if (maximo is None or num > maximo):
            maximo = num
    return maximo


def remove_iguais(lista, elemento):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == elemento:
            lista.pop(i)
    
    return lista


def remove_maiores(lista):
    remover = meu_max(lista)
    lista = remove_iguais(lista, remover)
    verifica = meu_in(lista, remover)
    if verifica == False: return None


lista1 = [8, 7, 3, 8, 2]
assert remove_maiores(lista1) == None
assert lista1 == [7, 3, 2]

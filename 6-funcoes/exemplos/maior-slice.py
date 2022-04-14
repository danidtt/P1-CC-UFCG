def maior_slice(lista):
    if lista == []:
        return []
    sublista = []
    sublista.append(lista[0])
    lista_aux = []
    for i in range(1, len(lista)):
        if lista[i - 1] > lista[i]:
            if len(sublista) >= len(lista_aux):
                lista_aux = sublista
            sublista = []
            sublista.append(lista[i])
        elif lista[i - 1] < lista[i]:
            sublista.append(lista[i])
        if i == len(lista) - 1 and len(sublista) >= len(lista_aux):
            lista_aux = sublista
    return lista_aux


assert maior_slice([1, 2, 3, 4, 2, 0, 1]) == [1, 2, 3, 4]
assert maior_slice([7, 6, 2, 9, 10]) == [2, 9, 10]
assert maior_slice([7, 8, 9, 1, 2, 3, 0]) == [1, 2, 3]

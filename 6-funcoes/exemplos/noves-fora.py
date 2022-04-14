def meu_slice(lista, começo, fim):
    listanova = []
    for i in range(começo, fim):
        listanova.append(lista[i])
    
    return listanova


def ordem_decrescente(lista):
    tamanho = len(lista)
    listanova = []
    while len(listanova) < tamanho:
        maior = lista[0]
        ind = 0
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                ind = i
        lista.pop(ind)
        listanova.append(maior)
    return listanova


def noves_fora(lista):
    novesfora = [lista]
    resto = 0
    
    if len(lista) == 1:
        if lista[0] < 9:
            resto = lista[0]
            return resto, novesfora
        else:
            novesfora.append([0])
            return resto, novesfora

    while True:
        if len(lista) == 1 and lista[0] < 9: break
        resto = (lista[0] + lista[1]) % 9
        lista = [resto] + meu_slice(lista, 2, len(lista))
        lista = ordem_decrescente(lista)
        novesfora.append(lista)

    return resto, novesfora

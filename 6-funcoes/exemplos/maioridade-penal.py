def maioridade_penal(nome, idade):
    lista = []
    nome = nome.split(' ')
    idade = idade.split(' ')
    for i in range(len(nome)):
        if int(idade[i]) >= 18:
            lista.append(nome[i])
    resultado = ''
    for l in range(len(lista)):
        # pega último indice da lista
        if l == len(lista) - 1:
            resultado += lista[l]   # se for o último, sem espaço
        # restante com espaço (primeiros)
        else: resultado += lista[l] + ' '
    return resultado


assert maioridade_penal("Jansen Italo Ana","14 21 60") == 'Italo Ana'

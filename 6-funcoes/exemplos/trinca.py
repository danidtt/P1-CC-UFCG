def remove(digitos):
    for (indice, valor) in enumerate(digitos):
        remover = []
        for (indice_compara, valor_compara) in enumerate(digitos):
            if valor == valor_compara - 1:
                remover.append(indice_compara)
                break
        if len(remover) == 1 :
            for (indice_compara, valor_compara) in enumerate(digitos):
                if valor == valor_compara - 2:
                    remover.append(indice)
                    remover.append(indice_compara)
                    break
        if len(remover) == 3:
            remover.sort()
            for i in range(len(remover)):
                digitos.pop(remover[-(i + 1)])
            return len(digitos)            


def trinca(digitos):
    while True:
        removeu = remove(digitos)
        if removeu == None:
            break


digitos = [1, 7, 2, 8, 5, 3]
assert trinca(digitos) == None
assert digitos == [7, 8, 5]

digitos = [1, 3, 2, 7, 3, 2, 1]
assert trinca(digitos) == None
assert digitos == [7]
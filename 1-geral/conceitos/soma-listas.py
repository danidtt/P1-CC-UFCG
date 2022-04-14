# Primeiro pares, depois impares

def par_impar(lista):
    par, impar = [], []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    return par + impar


lista = [1, 2, 3, 4]

print(par_impar(lista))
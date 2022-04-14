lista = [1, 4, 8, 3, 9, 10]
lista1 = [2, 4, 5]
lista2 = [1, 2, 2, 3]

# APPEND E POP
# adiciona
lista.append(10)
print(lista)
# remove
lista.pop(5) # indice[5]
print(lista)

def meu_remove(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            lista.pop(i)
            break
    return lista

def remove_iguais(lista, elemento):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == elemento:
            lista.pop(i)
    return lista

def meu_extend(lista1, lista2):
    for i in lista2:
        lista1.append(i)
    return lista1

print(meu_remove(lista, 3))
assert lista == [1, 4, 8, 9, 10]

print(f'Lista 1 = {lista1}')
print(f'Lista 2 = {remove_iguais(lista2, 2)}')
assert lista2 == [1, 3]

print(f'Lista 1 + Lista 2 = {meu_extend(lista1, lista2)}')
assert lista1 == [2, 4, 5, 1, 3]

def multiplica_lista(n, lista):
    nova_lista = []
    for i in range(n):
        for elemento in lista:
            nova_lista.append(elemento)
    return nova_lista


l = ['joao', 'pedro']
assert multiplica_lista(2, l) == ['joao', 'pedro', 'joao', 'pedro']

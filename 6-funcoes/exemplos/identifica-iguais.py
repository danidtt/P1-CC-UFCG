def identifica_iguais(lista1, lista2):
    for i in range(len(lista2)):
        if i == len(lista1): break
        if int(lista2[i]) == int(lista1[i]):
            print(f'{i + 1}: {lista1[i]}')


lista1 = input().split()
lista2 = input().split()

identifica_iguais(lista1, lista2)
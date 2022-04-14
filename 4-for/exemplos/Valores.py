lista1, lista2 = input().split(), input().split()

# N de indices da menor lista
if len(lista1) < len(lista2):
    menor_lista = len(lista1)
    maior_lista = len(lista2)
else:
    menor_lista = len(lista2)
    maior_lista = len(lista1)

# Iterar nos indices
soma = 0
for i in range(menor_lista):
    if lista1[i] == lista2[i]:
        soma += 1
        # i = posição
        print(f'i = {i}: {lista1[i]}') # indice[?] da lista

media = menor_lista + maior_lista
porcentagem = (soma / media) * 100
print(f'Valores coincidentes: {soma} ({porcentagem:.0f}%)')
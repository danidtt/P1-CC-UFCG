lista1 = input().split()
lista2 = input().split()

for i in range(len(lista2)):

    if i == len(lista1): break

    if int(lista2[i]) == int(lista1[i]):
        print(i)    # imprime posição na lista
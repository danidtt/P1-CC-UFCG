lista = [int(n) for n in input().split()]

soma = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        soma += lista[i]

print('For = ', soma)

# ou...

i = soma = 0  
while True:
    if i == len(lista) - 1: break
    if lista[i] % 2 == 0:
        soma += lista[i]
    i += 1

print('While = ', soma)

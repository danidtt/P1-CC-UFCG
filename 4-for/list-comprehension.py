lista, pares = [1, 2, 3, 4], []
for x in lista:
    if x % 2 == 0:
        pares.append(x)

print(f'Normal = {pares}')

pares = [x for x in lista if x % 2 == 0]

print(f'List comprehension = {pares}')
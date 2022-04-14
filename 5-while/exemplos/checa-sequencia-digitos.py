sequencia = input()
valor_limite = int(input())

criterio_de_parada = 'final da sequência'
i = 0
numeros_lidos = 0
soma = 0
impares = 0
while True:
    if i == len(sequencia): break
    numero = int(sequencia[i])
    numeros_lidos += 1
    soma += numero
    if numero % 2 != 0:
        impares += 1
        if impares >= 6:
            criterio_de_parada = '6 dígitos'
            break
    elif soma >= valor_limite:
        criterio_de_parada = 'limite'
        break
    i += 1

total = len(sequencia)

print(f'soma: {soma}')
print(f'números lidos: {numeros_lidos} de {total}')
print(f'critério de parada: {criterio_de_parada}')

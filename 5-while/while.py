# FOR DEFINE LIMITE

lista = []
for i in range(1, 10):
    lista.append(i)
print(f'For = {lista}')

# LOOP INFINITO
lista2 = []         # EQUIVALENTE A RANGE(1, 10):
i = 1               # define parametro / variavel
while i < 10:       # condição = break automatico
    lista2.append(i)        
    i += 1          # atualiza valor do parametro
print(f'While = {lista2}')

print('\n===For===')

for i in range(1, 3): # 1 até 2 (indice[3])
    n = int(input('Digite um número: '))
print('Fim')

print('\n===While===')

par = impar = 0
while n != 0:           # enquanto i for diferente de 0, execute
    n = int(input('Digite um número: '))
    if n != 0:          # para o programa não considerar o 0 como par
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'-----------\nPares = {par}\nImpares = {impar}')

print('\n===Usando end===')

count = 1
while count <= 10:
    print(count, end='...')
    count += 1
print('Fim')

print('\n===Soma de inputs===')

quantidade = soma = 0
while True:
    n = int(input('Type a number (999 to stop): '))
    if n == 999: break
    quantidade += 1
    soma += n
print(f'Números digitados = {quantidade}\nSoma dos números = {soma}')

print('\n===Tabuada===')

lista = list(range(1, 11))
while True:
    print('-------------')
    n = int(input('Número: '))
    print('-------------')
    if n < 0: break
    for i in lista:
        multiplica = n * i
        print(f'{n} x {i} = {multiplica}')

print('\n===Jogo: Ímpar ou Par===')

import random

par = impar = 0
while par < 2 and impar < 2:
    n = int(input('Digite um número: '))
    computador = random.random()
    soma = n + computador
    escolha = input('Par ou ímpar? [P/I] ')
    if soma % 2 == 0:
        par += 1
        if escolha == 'p':
            resposta = 'Você venceu'
        else:
            resposta = 'Você perdeu'
    else:
        impar += 1
        if escolha == 'i':
            resposta = 'Você venceu'
        else:
            resposta = 'Você perdeu'
print(resposta)

valor = int(input())
lista = input().split()

print(f'O número {valor} está na sequência?')

# resposta padrão caso o valor não seja encontrado
resposta = 'Não'

for n in lista:
    # se um número da lista for igual ao valor
    if int(n) == valor:   # cada elemento da lista de strings transformado em inteiros
        resposta = 'Sim'

print(resposta)
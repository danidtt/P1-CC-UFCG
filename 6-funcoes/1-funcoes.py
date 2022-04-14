# Funções servem para fazer algo apenas uma vez e chamar
# IMPORTANTE: 'return' para o programa, lembre de colocá-lo no final

print('Verifica se número é par:')

n = int(input())

def par():
    if num % 2 == 0:
        print(f'{num} é par')

i = 0
while i < n:
    num = int(input())
    par()
    i += 1

print('\nCalcula três equações de 2° grau:')

a1, b1, c1 = 6, 8, 2
a2, b2, c2 = 9, 24, 16
a3, b3, c3 = 1, -2, 4

def delta(a, b, c):
    return (b ** 2) - 4 * a * c

print(f'Delta 1 = {delta(a1, b1, c1)}')
print(f'Delta 2 = {delta(a2, b2, c2)}')
print(f'Delta 3 = {delta(a3, b3, c3)}')

print(f'\nDobrar listas:')

# Função que dobra valores de lista
def dobra(lista):
    nova_lista = []
    for i in lista:
        i *= 2
        nova_lista.append(i)
    return nova_lista

l1, l2, l3 = list(range(6)), [6, 7], [8, 9]

print(l1, l2, l3)
print(dobra(l1))
print(dobra(l2))
print(dobra(l3))

print('\nMinha função sum():')

def soma(lista):
    s = 0
    for i in lista:
        s += i
    return s

l1, l2, l3 = list(range(6)), [6, 7], [8, 9]

print(soma(l1))
print(soma(l2))
print(soma(l3))

# Assert = teste de True or False
assert soma([0, 1, 2]) == 3 # True
assert soma(l1) == 6        # False = vai dar erro































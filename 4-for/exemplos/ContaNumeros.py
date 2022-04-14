# a < b

# etapa 1: ler N
n = int(input())

# etapa 2: ler seq dados, criar lista
lista = []
for i in range(n):
    num = int(input()) # numeros inteiros para lista
    lista.append(num) # colocar numeros na lista

print('---')

# etapa 3: ler a, b
a, b = int(input()), int(input())

# etapa 4: classificar e contar por categorias
antes, entre, depois = 0, 0, 0
for num in lista:
    if num < a:
        antes += 1
    elif a < num < b:
        entre += 1
    elif b < num:
        depois += 1 

print(f'{antes} antes')
print(f'{entre} entre')
print(f'{depois} depois')

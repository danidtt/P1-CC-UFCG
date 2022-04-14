cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

format1 = cpf1 // 100
resto1 = cpf1 % 100
soma1 = (resto1 // 10) + (resto1 % 10)

format2 = cpf2 // 100
resto2 = cpf2 % 100
soma2 = (resto2 // 10) + (resto2 % 10)

format3 = cpf3 // 100
resto3 = cpf3 % 100
soma3 = (resto3 // 10) + (resto3 % 10)

print(f'{format1}-{resto1}')
print(soma1)

print(f'{format2}-{resto2}')
print(soma2)

print(f'{format3}-{resto3}')
print(soma3)

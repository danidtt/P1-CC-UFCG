print('Cálculo da Superfície de um Cilindro\n---')
diametro = float(input('Medida do diâmetro? '))
altura = float(input('Medida da altura? '))
pi = 3.14159

raio = diametro / 2
area = 2 * (pi * (raio ** 2)) + 2 * (pi * raio * altura)

print(f'---\nÁrea calculada: {area:.2f}')
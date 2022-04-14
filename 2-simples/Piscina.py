comprimento = float(input())
largura = float(input())
profundidade = float(input())

area = comprimento * largura
litros = profundidade * 1000
volume = area * litros

print(f'A piscina comporta {volume:.2f} litros de água.')
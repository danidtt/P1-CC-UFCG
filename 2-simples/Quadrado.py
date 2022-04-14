import math

lado = float(input())
r = math.sqrt(2 * ((lado / 2) ** 2))

perimetro = 2 * math.pi * r
area = 2 * math.pi * lado

print(f'{perimetro:.5f}')
print(f'{area:.5f}')

a = float(input())
b = float(input())
c = float(input())

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b) :
    perimetro = a + b + c
    print(f'triangulo valido. {perimetro:.0f}')
else:
    print('triangulo invalido.')
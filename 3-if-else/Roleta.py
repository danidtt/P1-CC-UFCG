x = int(input())

if x > 360:
    x = x % 360
if 0 < x < 90:
    print('Quadrante 1')
if 90 < x < 180:
    print('Quadrante 2')
if 180 < x < 270:
    print('Quadrante 3')
if 270 < x < 360:
    print('Quadrante 4')
if x == 0 or x == 90 or x == 180 or x == 270 or x == 360:
    print('Sobre eixos')
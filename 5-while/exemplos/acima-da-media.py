ssp = float(input())

while True:
    lista = []
    entrada = input()
    valores = entrada.split()
    if valores[0] == 'fim':
        break
    v = 0
    for i in valores:
        v += int(i)
    media = v / len(valores)
    if media > ssp:
        print(entrada)
    elif media * 2 < ssp:
        break

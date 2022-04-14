def soma_intervalo(a, b):
    if a <= b:
        soma = 0
        while a <= b:
            soma += a
            a += 1
    return soma


assert soma_intervalo(5,15) == 110
assert soma_intervalo(10,10) == 10

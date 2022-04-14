def seleciona_primos(lista):
    primos = []
    for num in lista:
        divisores = 0
        for divisor in range(1, num):
            if num % divisor == 0:
                divisores = divisores + 1
                if divisores > 1: break
        if divisores == 1:
            primos.append(num)
    
    return primos


lista = [3, 6, 9, 12, 15, 18, 19, 21]

assert seleciona_primos(lista) == [3, 19]
assert lista == [3, 6, 9, 12, 15, 18, 19, 21]

from p1 import Array


def insere(array, indice, elemento):
    for i in range(len(array) - 1, indice, -1):
        array[i] = array[i - 1]
    array[indice] = elemento


def insere_ordenado(array, num):
    for i in range(len(array)):
        if array[i] is None: break
        elif array[i] >= num:
            insere(array, i, num)
            return
    
    array[i] = num


a = Array(10)

for i in range(10):
    insere_ordenado(a, i * 10)

while True:
    entrada = input()
    if not entrada: break
    num = int(entrada)
    insere_ordenado(a, num)
    print(a)
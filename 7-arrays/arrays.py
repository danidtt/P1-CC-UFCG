from p1 import Array
from random import randint

# Já define quantidade de elementos da lista
a = Array(5)
print(a)

# Forma de adicionar: alterar
a[0] = 1
print(a)

# append, pop, insert, remove...não funcionam em arrays

# quantidade, elemento
a2 = Array(3, 0)
print(a2)
'''
    Pequeno programa exemplo:
    Gera lista de 10 elementos aleatórios entre 0 e 9
'''
def insere(array, indice, elemento):
    for i in range(9, indice, -1):
        array[i] = array[i - 1]
    array[indice] = elemento


def pop(array, indice):
    for i in range(indice, 9):
        array[i] = array[i + 1]
    array[9] = None


def main():
    a3 = Array(10)
    for i in range(10):
        a3[i] = randint(0, 9)

    print(a3)
    insere(a3, 2, 100)
    print(a3)
    pop(a3, 0)
    print(a3)


if __name__ == '__main__':
    main()
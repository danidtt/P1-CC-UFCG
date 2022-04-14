from p1 import Array
#
#
def funcao(parametro):
    return parametro * 2
#
#
lista = [1, 2, 3, 4]
#
nova_lista = []
for i in lista:
    dobrado = funcao(i)
    nova_lista.append(dobrado)
#
print(nova_lista)
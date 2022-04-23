# 1° importar módulos (import)
# 2° funções (def): 2 espaços, cima e baixo
# 3° variáveis
# 4° restante
# 5° formatação e impressão (print)
from math import sqrt
#
#
def funcao(parametro):
    resultado = sqrt(parametro * 2)
    return resultado
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

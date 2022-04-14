# Programa que determina a diferença de idade entre Maria e João
nome = ['Maria', 'João']
idade = [12.6, 15]
diferenca = idade[1] - idade[0]

# TIPOS DE FORMATAÇÃO
# Python 3.6
print(f'Existem dois irmãos chamados {nome[0]} e {nome[1]}.')
# Python 3
print('{} tem {} anos e {} tem {}.'.format(nome[0], idade[0], nome[1], idade[1]))
# Python 2
print('%s é %d anos mais velho que %s.' % (nome[1], diferenca, nome[0]))
# %s = string   %d = inteiro

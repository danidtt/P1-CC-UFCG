# EXEMPLO DE ALGORITMO

# Lucro Mensal

# Entrada:
#   - leitura e processamento de dados na memória
#       - criar duas listas: receitas e despesas
#       - usar um laço for que se repita 12 vezes (jan-dez) -> for i in range(12)
#           - ler linha de entrada
#           - usar o split() para separar receita de despesa -> lista str ['0', '1']
#           - converter as strings para float
#           - adicionar (.append) o float receita em receitas
#           - adicionar (.append) o float despesa em despesas 

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
receitas = []
despesas = []

for i in range(12):
    linha = input().split() # transformar entrada em lista de strings

    # separar índices da lista e transformar em float
    receita = float(linha[0])
    despesa = float(linha[1])

    # adicionar nas listas
    receitas.append(receita)
    despesas.append(despesa)

lucros = []
for i in range(12):
    lucros.append(receitas[i] - despesas[i])


                # range(12) -> meses
for i in range(len(lucros)):
    mes = meses[i]
    lucro = lucros[i]
    print(f'{mes} {lucro:.1f}')
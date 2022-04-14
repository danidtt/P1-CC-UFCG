adultos = int(input())
criancas = int(input())
ingresso = float(input())
ingresso_criancas = ingresso / 2

preco = (adultos * ingresso) + (criancas * ingresso_criancas)

print(f'Total: R$ {preco:.2f}')
from math import floor

capacidade = int(input())
peso_medio = int(input())

pessoas = capacidade / peso_medio
numero = floor(pessoas) 

print(f'O elevador pode transportar {numero:.0f} pessoas com segurança.') 
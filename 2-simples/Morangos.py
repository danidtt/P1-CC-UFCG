morangos = int(input())

caixas = morangos // 400 
porcentagem = 100 - ((caixas * 400 * 100) / morangos)  

print(f'{caixas:.0f} caixa(s) completa(s) para embalar os morangos.')
print(f'{porcentagem:.1f}% dos morangos serão perdidos.')
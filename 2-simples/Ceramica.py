capacidade_caixa = float(input('Capacidade de revestimento? '))

print('\n== Dados do vão a revestir ==')

comprimento = float(input('Comprimento? '))
largura = float(input('Largura? '))
altura = float(input('Altura? '))

area_parede = (comprimento * altura) * 4
area_chao = comprimento * largura
area_total = area_parede + area_chao

caixas = area_total // capacidade_caixa

print('\n== Resultados ==')
print(f'Área total a revestir: {area_total} m2')
print(f'Número de caixas: {caixas:.0f}')
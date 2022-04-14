def calcula_venda(valor, ipi, iof, lucro):
    porcentagem = (valor * ipi) + (valor * iof) + (valor * lucro)
    saida = valor + porcentagem
    return saida


while True:

    entrada = input()
    if entrada == '-': break
    lista = entrada.split(', ')
        
    valor = float(lista[0])
    ipi = float(lista[1])
    iof = float(lista[2])
    lucro = float(lista[3])

    saida = calcula_venda(valor, ipi, iof, lucro)

    print(f'O valor de venda para este produto deve ser R$ {saida:.2f}')


assert calcula_venda(50.0, 0.1, 0.1, 0.1) == 65.0
assert calcula_venda(80.0, 0.1, 0.3, 0.4) == 144.0
assert calcula_venda(60.0, 0.2, 0.5, 0.4) == 126.0
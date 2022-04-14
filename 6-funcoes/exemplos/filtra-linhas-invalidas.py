def meu_join(delimitador, sequencia_de_string):
    assert len(sequencia_de_string) > 0
    joinfinal = ''    

    for i in range(len(sequencia_de_string)):
        if i < len(sequencia_de_string) - 1:
            joinfinal += f'{sequencia_de_string[i]}{delimitador}'
        else:
            joinfinal += str(sequencia_de_string[i])
    
    return joinfinal


linha = 1
invalidas = 0
while True:
    entrada = input().split()
    if entrada[0] == 'fim': break

    par, impar = 0, 0
    for i in range(len(entrada)):
        if int(entrada[i]) % 2 == 0:
            par += 1
        else: impar += 1

    if impar >= par:
        sequencia = meu_join(' ', entrada)
        invalidas += 1
        print(f'linha {linha} inválida: {sequencia}')
    
    linha += 1

print(f'sequências lidas: {linha - 1} (inválidas: {invalidas})')
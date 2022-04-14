def multiplica(cpf):
    resultado = 0
    vezes = 2
    for i in range(len(cpf) - 1, -1, -1):
        resultado += int(cpf[i]) * vezes
        vezes += 1
    calculo = (10 * resultado) % 11
    if calculo == 10:
        calculo = 0
    return calculo


def calcula_digitos_verificacao(cpf):
    primeiro_digito = str(multiplica(cpf))
    segundo_digito = str(multiplica(cpf + primeiro_digito))
    return primeiro_digito + segundo_digito


assert calcula_digitos_verificacao('153245875') == '40'
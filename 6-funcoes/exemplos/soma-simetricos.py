def soma_simetricos(valores):
    retorno = []
    if len(valores) % 2 == 1:
        retorno.append(valores[int(len(valores)  / 2 - 0.5)])
        valores.pop(int(len(valores) / 2 - 0.5))
    
    auxiliar = []
    for i in valores:
        auxiliar.append(i + valores[-1])
        valores.pop()

    return auxiliar + retorno
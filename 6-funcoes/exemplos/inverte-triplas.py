def inverte3a3(s):
    lista = []
    nova_s = ''

    count = 0
    for i in range(len(s)):
        
        if count == 3:
            lista.append(nova_s)
            nova_s = ''
            count = 0
        
        count += 1
        nova_s += s[i]

    lista.append(nova_s)

    saida = ''
    for i in range(len(lista) -1, -1, -1):
        saida += lista[i]

    return saida


assert inverte3a3("abcdef") == "defabc"

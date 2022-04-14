def meu_split(frase, delimitador):
    str_vazia = ''
    splitted = []
    for letra in frase:
        if letra != delimitador:
            str_vazia += letra
        else:
            if str_vazia == '':
                str_vazia = '' 
            else:
                splitted.append(str_vazia)
                str_vazia = ''
    if str_vazia:
        splitted.append(str_vazia)
    return splitted


def is_substring_expr(str1, str2):
    lista = meu_split(str2, '*') # [oi, voce]
    esta = 0
    verifica = False

    for i in range(len(lista[0])):
        if str1[i] == lista[0][i]:
            esta += 1
    if esta == len(lista[0]): verifica = True

    validacao = False
    indice = len(str1) - 1
    esta = 0
    for i in range(len(lista[1]) - 1, -1, -1):
        if str1[indice] == lista[1][i]:
            esta += 1
            indice -= 1

    if esta == len(lista[1]): validacao = True
    if validacao and verifica: return True
    else: return False
    

assert is_substring_expr('oicarovoce','oi*voce')
assert is_substring_expr('oicvoce','oi*voce')

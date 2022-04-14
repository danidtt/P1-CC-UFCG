def cesar(msg, d):
    convertido = ''
    for i in msg:
        # se não for letra minúscula, adicione elemento
        if ord(i) < 97 or ord(i) > 122:
            convertido += i
        else:          
            posicao = ord(i) - ord('a')   # 101 - 97 = 4
            muda_posicao = (posicao + d) % 26   # 26 letras do alfabeto minúsculas
            convertido += chr(muda_posicao + ord('a'))   # 2 + 97(a partir de onde começa) = 99 --> 'c'

    return convertido

assert cesar("exemplo", 4) == "ibiqtps"
assert cesar("Exemplo 2!", 4) == "Ebiqtps 2!"
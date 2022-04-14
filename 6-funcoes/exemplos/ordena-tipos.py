def ordena_tipos(lista):
    inteiros, palavras, resto = [], [], []
    for i in lista:
        if i.isdigit():
            inteiros += [i]
        elif i.isalpha():
            palavras += [i]
        else:
            resto += [i]

    return inteiros + palavras + resto


assert ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8']) \
       == ['2', '4', '8', 'e', '1a', '4.4', 'e6']
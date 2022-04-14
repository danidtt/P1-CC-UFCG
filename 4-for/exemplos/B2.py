binario = input()

        # número de indices
indices = len(binario) - 1

x = 0
       # quantidade de indices a partir do último [-1]
for i in binario:
    # vai multiplicando os próximos indices por 2
    multiplica = 2 ** indices
    calculo = int(int(i) * multiplica)

    print(f'{i} * {multiplica} = {calculo}')

    x += calculo
    indices -= 1  

print(f'{binario}(2) = {x}(10)')
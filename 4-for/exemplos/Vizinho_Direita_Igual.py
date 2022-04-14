sequencia = input().split()

contador = 0
for i in range(len(sequencia) - 1):
    if sequencia[i] == sequencia[i + 1]:
        contador += 1

print(contador)

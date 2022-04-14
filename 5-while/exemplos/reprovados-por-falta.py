reprov = 0

while True:
    entrada = input()
    if entrada == '-': break
    i = 0
    count = 0
    while i < len(entrada):
        if entrada[i] == 'f':
            count += 1
            if count > 8:
                reprov += 1
                break
        i += 1

print(reprov, 'aluno(s) reprovado(s) por falta.')

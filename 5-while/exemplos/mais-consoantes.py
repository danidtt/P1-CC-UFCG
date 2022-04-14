saida = 0

while True:
    vogal = consoante = 0
    entrada = input()
    for i in entrada:
        if i in 'aeiouAEIOU':
            vogal += 1
        else:
            consoante += 1
    saida += 1
    if consoante > vogal: break
    
print(saida)

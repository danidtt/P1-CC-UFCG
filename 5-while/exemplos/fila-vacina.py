sim_seguiram = 0
nao_seguiram = 0

while True:
    fila = input()
    if fila == "###": break
    i = 0
    while True:
        if fila[i] == "a" and fila[i + 1] == "i":
            nao_seguiram += 1
            break
        if fila[i] == "a" and fila[i + 1] == "c":
            nao_seguiram += 1
            break
        i += 1
        if i == len(fila) - 1:
            sim_seguiram += 1
            break

print(f"sim: {sim_seguiram}")
print(f"não: {nao_seguiram}")

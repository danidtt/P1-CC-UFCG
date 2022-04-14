frase = input()
chave = input()

senha_decodificada = ""
for i in range(len(frase)):
    if 0 <= int(frase[i]) <= 9:
        senha_decodificada += chave[i]
    else:
        senha_decodificada += frase[i]

print(senha_decodificada)

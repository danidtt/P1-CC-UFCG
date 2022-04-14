numeros = input().split()

tem_cinco = 0

for numero in numeros:
    contador = 0
    impares = []
    for i in range(len(numero)):        
        validacao = False
        for n in impares:
            if n == numero[i]:
                validacao = True
    
        if int(numero[i]) % 2 != 0 and validacao == False:
            contador += 1
            impares.append(numero[i])
    
            if contador == 5:
                tem_cinco += 1
        

print(tem_cinco)
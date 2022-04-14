sequencia = input().split()
numero = int(input())

validacao = False
for num in sequencia:
    if int(num) == int(numero):
        validacao = True
        break

if validacao == False:
    print("não")
else:
    print("sim")

soma_jogadores = 0
while True:
    entrada = input()
    if entrada == '-': break
    soma_jogadores += 1

if soma_jogadores == 11:
    print("Modalidade -> Futebol")
elif soma_jogadores == 5:
    print("Modalidade -> Basquete")
elif soma_jogadores == 6:
    print("Modalidade -> Vôlei")
elif soma_jogadores == 7:
    print("Modalidade -> Handebol")

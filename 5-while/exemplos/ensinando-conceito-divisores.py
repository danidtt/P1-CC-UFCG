divisor = int(input())

while True :
    divide = 0
    for r in range(3):
        dividendo = int(input())
        if divisor > dividendo:
            if divisor % dividendo != 0:
                divide += 1
        else:
            if dividendo % divisor != 0:
                divide += 1
    if divide == 0:
        print("Acertou! Parabéns!")
        break
    elif divide == 1:
        print("Quase lá, tente novamente!")
    else:
        print("Tem que melhorar, tente novamente!")
    divide = 0


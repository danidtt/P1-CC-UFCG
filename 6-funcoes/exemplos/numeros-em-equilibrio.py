impar, par = [], []
diferenca = 0

while True:
    num = int(input())
    if num % 2 == 0:
        par.append(num)
        diferenca += 1
    else:
        impar.append(num)
        diferenca -= 1

    if diferenca > 2 or diferenca < -2: break

maior = ""
if len(impar) > len(par):
    maior = "IMPARES"
else:
    maior = "PARES"

print(f"{maior} em maior quantidade")

print("PARES:")

for i in par:
    print(i)

print("IMPARES:")

for i in impar:
    print(i)
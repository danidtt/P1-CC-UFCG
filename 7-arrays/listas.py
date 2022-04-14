def insere_ordenado(array, num):
    for i in range(len(array)):
        if array[i] >= num:
            array.insert(i, num)
            return
    
    array.append(num)


a = []

while True:
    entrada = input()
    if not entrada: break
    num = int(entrada)
    insere_ordenado(a, num)
    print(a)
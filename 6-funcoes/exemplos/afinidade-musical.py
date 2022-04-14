def tem_afinidade(l1, l2):
    igual = 0
    for i in l1:
        for j in l2:
            if i == j:
                igual += 1
    if igual >= 3: return True
    else: return False


l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True

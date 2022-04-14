def filas_de_atendimento(fila_unica, n) :
    filas = []
    for _ in range(n) :
        filas.append([])

    suporte = 0
    for i in fila_unica :
        filas[suporte].append(i)
        suporte += 1
        if suporte == n :
            suporte = 0
    
    return filas


pacientes = ['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
assert filas_de_atendimento(pacientes, 3) == [
    ['Andre', 'Carlos'],
    ['Antonio', 'Claudia'],
    ['Bianca']
]

pacientes = ['Andre', 'Antonio', 'Bianca', 'Carlos']
assert filas_de_atendimento(pacientes, 2) == [
    ['Andre', 'Bianca'],
    ['Antonio', 'Carlos']
]
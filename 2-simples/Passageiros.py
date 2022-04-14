passageiros = int(input())
capacidade = int(input())

van = passageiros // capacidade
sobra = passageiros % capacidade
porcentagem = (sobra / passageiros) * 100

print(f'{van} van(s) completa(s).')
print(f'{porcentagem:.2f}% dos passageiros não utilizarão vans.')
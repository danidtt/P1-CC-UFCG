area_casa = float(input('Área construída? '))
aliquota = float(input('Alíquota? '))

iptu = (area_casa * aliquota) + 35
cota_unica = iptu - (iptu * 0.25)
parcelas_6 = iptu - (iptu * 0.05)  

vezes_6 = parcelas_6 / 6
vezes_10 = iptu / 10

print(f'IPTU: R$ {iptu:.2f}\n')
print(f'Pagamento:\n1. Quota única. R$ {cota_unica:.2f}')
print(f'2. Em 6 parcelas. Total: R$ {parcelas_6:.2f}\n   6 x R$ {vezes_6:.2f}')
print(f'3. Em 10 parcelas. Total: R$ {iptu:.2f}\n   10 x R$ {vezes_10:.2f}')
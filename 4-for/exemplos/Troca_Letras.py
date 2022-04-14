# Trocar vogais por 0

senha = 'casa'
nova = ''

for letra in senha:

    if letra in 'AEIOUaeiou':
        nova += '0'       # nova = nova + 1
        
    else:
        nova += letra

print(nova)
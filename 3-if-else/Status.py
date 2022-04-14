nota = float(input())

if nota < 4 or nota >= 7:
    print(f'média final: {nota:.1f}')
elif nota >= 4 or nota < 7:
    rec = float(input())
    media = ((nota * 6) + (rec * 4)) / (6 + 4)
    print(f'média final: {media:.1f}')
renda = float(input())

if renda >= 0.00 and renda <= 2000.00:
    print('Isento')
elif renda >= 2000.01 and renda <= 3000.00:
    print(f'R$ {renda*(8/100):.2f}')
elif renda >= 3000.01 and renda <= 4500.00:
    print(f'R$ {renda*(12/100):.2f}')
elif renda > 4500:
    print(f'R$ {renda*(12/100):.2f}')
cru = int(input())

ano = int(cru/365)
cru = cru-(ano*365)

mes = int(cru/30)
cru = cru-(mes*30)

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{cru} dia(s)')
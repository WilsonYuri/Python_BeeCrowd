valor = float(input())

cem = int(valor/100)
valor = valor-(cem*100)

cin = int(valor/50)
valor = valor-(cin*50)

vin = int(valor/20)
valor = valor-(vin*20)

dez = int(valor/10)
valor = valor-(dez*10)

cic = int(valor/5)
valor = valor-(cic*5)

doi = int(valor/2)
valor = valor-(doi*2)

um = int(valor)
valor = valor-(um)

cinCen = int(valor/0.50)
valor = valor-(cinCen*0.50)

vinCen = int(valor/0.25)
valor = valor-(vinCen*0.25)

dezCen = int(valor/0.10)
valor = valor-(dezCen*0.10)

cicCen = int(valor/0.05)
valor = valor-(cicCen*0.05)

valor = round(valor, 2)
umCen = int(round(valor/0.01, 0))

print('NOTAS:')
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cin} nota(s) de R$ 50.00')
print(f'{vin} nota(s) de R$ 20.00')
print(f'{dez} nota(s) de R$ 10.00')
print(f'{cic} nota(s) de R$ 5.00')
print(f'{doi} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1.00')
print(f'{cinCen} moeda(s) de R$ 0.50')
print(f'{vinCen} moeda(s) de R$ 0.25')
print(f'{dezCen} moeda(s) de R$ 0.10')
print(f'{cicCen} moeda(s) de R$ 0.05')
print(f'{umCen} moeda(s) de R$ 0.01')
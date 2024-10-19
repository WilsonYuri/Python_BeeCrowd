
valor=int(input())

print(valor)

cem = int(valor/100)
valor = valor-(cem*100)

cin = int(valor/50)
valor = valor-(cin*50)

vin = int(valor/20)
valor = valor-(vin*20)

dez = int(valor/10)
valor = valor-(vin*10)

cic = int(valor/5)
valor = valor-(cic*5)

doi = int(valor/2)
valor = valor-(doi*2)

print(f'{cem} nota(s) de R$ 100,00')
print(f'{cin} nota(s) de R$ 50,00')
print(f'{vin} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cic} nota(s) de R$ 5,00')
print(f'{doi} nota(s) de R$ 2,00')
print(f'{valor} nota(s) de R$ 1,00')
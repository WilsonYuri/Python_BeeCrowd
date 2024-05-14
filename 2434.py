menor = 0
periodo, saldo  = map(int,input().split())
menor = saldo
i = 1
while i <= periodo:
    i += 1
    a = int(input())
    saldo = saldo + a
    if saldo < menor:
        menor = saldo
        
print(menor)
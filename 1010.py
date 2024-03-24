cod1, qnt1, val1 = map(float,input().split())
cod2, qnt2, val2 = map(float,input().split())

print(f'VALOR A PAGAR: R$ {(qnt1*val1)+(qnt2*val2):.2f}')
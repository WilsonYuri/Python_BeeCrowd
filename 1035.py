a,b,c,d = map(int,input().split())
pontos = 0
  
if b > c and d > a and (c + d)>(a + b) and c > 0 and d> 0 and a % 2 is 0:
    print('Valores aceitos')
    
else:
    print('Valores nao aceitos')
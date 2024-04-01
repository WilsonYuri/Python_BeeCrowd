p1,c1,p2,c2 = map(int,input().split())

lado1 = p1*c1
lado2 = p2*c2

if lado1 == lado2:
    print('0')
    
elif lado1 > lado2:
    print('-1')
    
else:
    print('1')
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

count = 0
soma = 0

if a > 0:
    count += 1
    soma += a
    
if b > 0:
    count += 1   
    soma += b

if c > 0:
    count += 1
    soma += c
    
if d > 0:
    count += 1  
    soma += d
    
if e > 0:
    count += 1
    soma += e
    
if f > 0:
    count += 1
    soma += f
    
media = soma/count
print(f'{count} valores positivos')
print(f'{media:.1f}')

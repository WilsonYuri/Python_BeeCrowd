def par(num):
    if num % 2 == 0:
        return 1
    else:
        return 0

pares = 0

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


if par(a) == 1:
    pares += 1
    
if par(b) == 1:
    pares += 1
    
if par(c) == 1:
    pares += 1
    
if par(d) == 1:
    pares += 1
    
if par(e) == 1:
    pares += 1
    
print(f'{pares} valores pares')

a,b,c = map(int,input().split())

if a > b and a > c:
    pos1 = a
    if b > c:
        pos2 = b
        pos3 = c
    else:
        pos2 = c
        pos3 = b

elif b > a and b > c:
    pos1 = b
    if a > c:
        pos2 = a
        pos3 = c
    else:
        pos2 = c
        pos3 = a
    
else:
    pos1 = c
    if a > b:
        pos2 = a
        pos3 = b
    else:
        pos2 = b
        pos3 = a
        
print(pos3)
print(pos2)
print(pos1)
print('')
print(pos1)
print(pos2)
print(pos3)
tries = int(input())

intw = 0
outtw = 0

i = 0

while i < tries:
    i += 1
    a = int(input())
    if a >= 10 and a <= 20:
        intw += 1
    else:
        outtw += 1
    
    
print(f'{intw} in')
print(f'{outtw} out')

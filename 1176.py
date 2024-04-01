ifib = 2
fib = [0, 1, 2]
while ifib <- 100:
    fib.append(fib[ifib] + fib[(ifib-1)])
    ifib += 1


times = int(input())
i = 0
ans = []
while i <= times:
    a = int(input())
    print(f'fib{a} = {fib[a]}')
    i += 1
    
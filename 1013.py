a,b,c = map(int,input().split())

maiorAB = int(((a+b+abs(a-b))/2))
maiorABC = int(((maiorAB+c+abs(maiorAB-c))/2))

print(f'{maiorABC} eh o maior')
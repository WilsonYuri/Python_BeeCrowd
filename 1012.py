a,b,c = map(float,input().split())

pi = 3.14159

areaTriangulo = ((1/2)*a*c)
areaCirculo =  (pi*(c*c))
areaTrapezio = (((a+b)/2)*c)
areaQuadrado = (b*b)
areaRetangulo = (a*b)

print(f'TRIANGULO: {areaTriangulo:.3f}')
print(f'CIRCULO: {areaCirculo:.3f}')
print(f'TRAPEZIO:{areaTrapezio:.3f}')
print(f'QUADRADO: {areaQuadrado:.3f}')
print(f'RETANGULO: {areaRetangulo:.3f}')
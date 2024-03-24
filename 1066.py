# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

par = 0
impar = 0
pos = 0
neg = 0

#par


if a % 2 is 0:
    par += 1
    
if b % 2 is 0:
    par += 1
if c % 2 is 0:
    par += 1
    
if d % 2 is 0:
    par += 1
    
if e % 2 is 0:
    par += 1

#impar

if a % 2 is not 0:
    impar += 1
    
if b % 2 is not 0:
  impar += 1
  
if c % 2 is not 0:
    impar += 1
    
if d % 2 is not 0:
  impar += 1
  
if e % 2 is not 0:
    impar += 1
    
#pos

if a > 0:
    pos += 1
    
if b > 0:
    pos += 1
    
if c > 0:
    pos += 1
    
if d > 0:
    pos += 1
    
if e > 0:
    pos += 1
    
#neg

if a < 0:
    neg += 1
    
if b < 0:
    neg += 1
    
if c < 0:
    neg += 1
    
if d < 0:
    neg += 1
    
if e < 0:
    neg += 1


print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')
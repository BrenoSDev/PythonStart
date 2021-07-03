#Os n primeiros primos
from time import sleep
print('Digite um valor n e nós mostraremos os n primeiros primos!')
n = int(input('Digite um valor: '))
while n <= 0:
	print('\033[1;31mDigite apenas valores positivos maiores que 0!\033[m')
	n = int(input('Digite um valor: '))
c = 0
primos = 2
print('\nOs %d primeiros primos são:'%n)
while c < n:
    divisores = 1
    divisor = 2
    while divisor <= primos:
        if primos % divisor == 0:
            divisores += 1
        divisor += 1
    if divisores == 2:
        print('%d'%primos)
        c += 1
    primos += 1
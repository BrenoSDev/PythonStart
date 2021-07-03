#Verificador de números primos
print('Digite um valor e nós diremos se ele é primo ou não!')
n = int(input('Digite um número: '))
while n <= 0:
    print('\033[31mDigite apenas valores positivos maiores que 0!\033[m')
    n = int(input('Digite um número: '))
c = 2
divisores = 1
while c <= n:
    if n % c == 0:
        divisores += 1
    c += 1
if divisores == 2:
    print('O número %d é primo!'%n)
else:
    print('O número %d não é primo!'%n)
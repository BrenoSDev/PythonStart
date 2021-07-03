#Cálculo da raiz quadrada usando o método de Newton
print('Digite um valor e nós calcularemos a raiz quadrade dele')
n = int(input('Digite um valor: '))
while n < 0:
    print('VALOR INCORRETO! Digite apenas valores positivos!')
    n = int(input('Digite um valor: '))
b = 2
while True:
	p = (b+(n/b))/2
	if p**2 - n < 0.0001:
		break
	b = p
print('A raiz quadrada de %d é %.2f'%(n, p))
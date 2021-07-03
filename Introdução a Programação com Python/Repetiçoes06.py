#Impressão de números pares de 0 até um número digitado pelo usuário
fim = int(input('Digite o último número a imprimir: '))
x = 0
while x <= fim:
	if x % 2 == 0:
		print(x)
	x += 1
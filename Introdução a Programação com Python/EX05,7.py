#Tabuada especificada pelo usuário
print('Digite um valor e a tabuada dele será mostrada na tela!')
n = int(input('Tabuada de: '))
início = int(input('Por qual valor você quer multiplicar primeiro: '))
fim = int(input('Por qual valor você quer multiplicar por último: '))
while início <= fim:
	print('%d x %d = %d'%(n, início, n*início))
	início += 1
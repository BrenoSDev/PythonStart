#Tabuada simples
print('Digite um valor e a tabuada dele será mostrada na tela!')
n = int(input('Tabuada de: '))
f = 1
while f <= 10:
	print('%d x %d = %d'%(n, f, n*f))
	f += 1
#Cálculo de média com acumulador
x = 1
soma = 0
while x <= 5:
	n = int(input('Digite o %dº número: '%x))
	soma += n
	x += 1
print('Média: %5.2f'%(soma/5))

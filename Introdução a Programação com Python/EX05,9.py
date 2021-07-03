#Divisão inteira de dois números usando apenas subtração
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
dividendo = n1
quociente = 0
while dividendo >= n2:
	dividendo -= n2
	quociente += 1
print('%d / %d = %d'%(n1, n2, quociente))
print('O resto da divisão é igual a %d'%dividendo)
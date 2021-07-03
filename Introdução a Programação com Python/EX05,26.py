#Resto da divisão entre dois números usando apenas soma e subtraçao
n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite um valor inteiro: '))
resto = n1
quociente = 0
while resto >= n2:
	resto -= n2
	quociente += 1
print('%d / %d = %d'%(n1, n2, quociente))
print('O resto da divisão entre %d e %d é %d'%(n1, n2, resto))
#Impressão de índices usando a função enumerate
L = [5,9,13]
for x, e in enumerate(L):
	print('[%d] %d'%(x,e))
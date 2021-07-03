#Impressão de índices sem usar a função enumerate
L = [5,9,13]
x=0
for e in L:
	print('[%d] %d'%(x,e))
	x += 1
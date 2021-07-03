#Usando enumerate e imprimindo a tupla
L = [5,9,13]
for z in enumerate(L):
	x,e = z
	print('[%d] %d'%(x,e))
	print(z)
#Pesquisa sequencial de dois valores
L = [12, 23, 27, 39, 53, 65, 69, 73, 74]
p = int(input('Digite o valor a procurar: '))
v = int(input('Digite outro valor a procurar: '))
x = 0
while x < len(L):
	if L[x] == p:
		break
	x += 1
y = 0
while y < len(L):
	if L[y] == v:
		break
	y += 1
if x < len(L) and y < len(L):
	if x < y:
		print('O valor %d foi encontrado primeiro!'%p)
	else:
		print('O valor %d foi encontrado primeiro!'%v)
	print('O valor %d foi encontrado na posição %d e o valor %d na posição %d'%(p, x, v, y))
elif x == len(L) and y < len(L):
    print('O valor %d não foi encontrado!'%p)
    print('O valor %d foi encontrado na posição %d'%(v, y))
elif y == len(L) and x < len(L):
    print('O valor %d não foi encontrado!'%v)
    print('O valor %d foi encontrado na posição %d'%(p, x))
else:
	print('Nenhum dos dois valores foi encontrado!')	
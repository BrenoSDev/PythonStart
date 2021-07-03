#Adição de elementos à lista usando for
L = []
while True:
	n = int(input('Digite um número (0 sai): '))
	if n == 0:
		break
	L.append(n)
for v in L:
	print(v)
    
#O primeiro While não pode ser transformado em for porque não se sabe o total de vezes que será necessário utilizar a repetição
#Já o segundo while pôde ser substituído porque ele só vai variar até passar por todos os elementos da lista L
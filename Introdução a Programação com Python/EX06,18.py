#Gerando dicionário com total de caracteres de cada tipo
caracteres = {}
frase = input('Digite uma frase: ')
espaço = 0
for c in frase:
	if c in caracteres:
		caracteres[c] += 1
	elif c == ' ':
		espaço += 1
	else:
		caracteres[c] = 1
print('Total de espaços: %d'%espaço)
print('%s ->'%frase, caracteres)
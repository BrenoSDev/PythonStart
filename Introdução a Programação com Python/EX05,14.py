#Soma e média aritmética de números diigitados em estrutura de repetição
c = 0
soma = 0
while True:
	n = int(input('Digite um valor ou 0 para sair: '))
	if n == 0:
		break
	soma += n
	c += 1
print('Você digitou %d valores!'%c)
print('A soma entre eles é %d e a média aritmética é igual a %.1f'%(soma, soma/c))
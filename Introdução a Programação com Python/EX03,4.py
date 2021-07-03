salário = float(input('Digite o seu salário: R$'))
imposto = salário > 1200
if imposto == True:
	print('Você precisa pagar imposto')
else:
	print('Parabéns! Você está isento do imposto.')
salário = float(input('Digite o valor do salário para cálculo do aumento: '))
if salário > 1250:
	aumento = 10
if salário <= 1250:
	aumento = 15
novo_salário = (100+aumento)*salário/100
print('Seu antigo salário era de R$%.2f. Com um aumento de %d porcento, ele passará a ser de R$%.2f.'%(salário, aumento, novo_salário))
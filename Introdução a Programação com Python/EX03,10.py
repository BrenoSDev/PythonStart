salário = float(input('Salário atual: '))
aumento = int(input('Porcentagem de aumento: '))
novo_salário = (100 + aumento)*salário / 100
print('Com um aumento de %d porcento, seu novo salário será de R$%.2f!'%(aumento, novo_salário))
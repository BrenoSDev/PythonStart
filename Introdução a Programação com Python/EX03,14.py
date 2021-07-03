#Cálculo de preço a pagar por aluguel de carro
distância = float(input('Quantidade de km percorridos: '))
dias = int(input('Dias de aluguel: '))
preço = dias*60 + 0.15*distância
print('O preço total do aluguel do carro é igual a R$%.2f!'%preço)
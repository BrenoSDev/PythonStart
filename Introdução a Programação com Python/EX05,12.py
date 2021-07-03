#Rendimento da poupança com depósitos mensais
print('Bem vindo ao Banco do Programador! Aqui a sua poupança rende mais!')
depósito = float(input('Digite o valor do depósito inicial na poupança: R$'))
taxa = float(input('Digite a taxa de juros da poupança: '))
mês = 1
montante = depósito
soma = depósito
while mês <= 24:
    montante *= (taxa/100)+1
    depósito = float(input('Digite o valor depositado na poupança no mês %d: '%mês))
    montante += depósito
    soma += depósito
    print('Mês %d: R$%.2f'%(mês, montante))
    mês += 1
print('0s total de juros ganhos no período foi igual a R$%.2f'%(montante-soma))
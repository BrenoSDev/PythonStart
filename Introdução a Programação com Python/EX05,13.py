#Quitação de uma dívida
dívida = float(input('\033[1;34;107mQual o valor total da sua dívida: R$'))
taxa = float(input('Qual a taxa de juros(%): '))
parcela = float(input('Quanto você pagará por mês: \033[m'))
total_pago = 0
valor_inicial = dívida
m = 0
while dívida > 0:
    dívida*= ((taxa/100)+1)
    if dívida < parcela:
        total_pago += dívida
        dívida -= dívida
    else:
        total_pago += parcela
        dívida -= parcela
    m += 1
print('Você pagará a sua dívida em %d meses, o total pago será de R$%.2f'%(m, total_pago)) 
print('O total de juros pagos será de R$%.2f'%(total_pago - valor_inicial))
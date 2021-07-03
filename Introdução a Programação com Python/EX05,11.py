#Rendimento da poupança
import time
print('Bem vindo ao Banco do Programador!')
depósito = float(input('Digite o depósito inicial na poupança: '))
taxa = float(input('Digite a porcentagem do valor da taxa de juros: '))
mês = 1
montante = depósito
while mês <= 24:
    montante *= (taxa/100) + 1
    time.sleep(0.2)
    print('Mês %d = R$%.2f'%(mês,montante))
    mês += 1
print('O total de juros ganhos no período foi de R$%.2f'%(montante - depósito))
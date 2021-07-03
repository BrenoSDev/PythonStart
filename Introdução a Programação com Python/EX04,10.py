#Preço pelo fornecimento de energia elétrica
consumo = float(input('Quantidade de kWh consumida: '))
instalação = input('Tipos de instalação: \n.R para residências \n.I para indústrias \n.C para comércios \nDigite o seu tipo de instalação: ').upper()
if instalação == 'R':
    if consumo <= 500:
        preço = 0.40
    else: 
        preço = 0.65
elif instalação == 'C':
    if consumo <= 1000:
        preço = 0.55
    else:
        preço = 0.60
elif instalação == 'I':
    if consumo <= 5000:
        preço = 0.55
    else: 
        preço = 0.60
else:
    print('Instalação inexistente! Por favor digite R para residencial, C para comercial e I para industrial')
    preço = 0
    consumo = 0
print('Você pagará R$%.2f pelo consumo de %.1f kWh'%(preço*consumo, consumo))

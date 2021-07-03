#Máquina registradora simples
total_compra = 0
produtos = 0
while True:
    código = int(input('Digite o código do produto ou 0 para sair: '))
    while código != 0 and código != 1 and código != 2 and código != 3 and código != 5 and código != 9:
        print('\033[1;31mERRO! Código Inválido!\033[m')
        código = int(input('Digite o código do produto ou 0 para sair: '))
    if código == 0:
        break
    elif código == 1:
        preço = 0.5
    elif código == 2:
        preço = 1
    elif código == 3:
        preço = 4
    elif código == 5:
        preço = 7
    elif código == 9:
        preço = 8
    quantidade = int(input('Quantas unidades você deseja comprar: '))
    total_compra += (quantidade*preço)
    produtos += quantidade
print('Você comprou %d produtos e a sua compra deu R$%.2f'%(produtos, total_compra))
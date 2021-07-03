#Aprovação de empréstimo bancário para compra de uma casa
casa = float(input('Digite o valor da casa: R$'))
salário = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Digite o total de anos a pagar: '))
prestação = casa / (anos*12)
if prestação > salário*0.3:
    print('O empréstimo não poderá ser concedido, pois a prestação de R$%.2f é maior do que 30 porcento do seu salário'%prestação)
else:
    print('O empréstimo foi concedido com sucesso!')
    print('O valot da prestação será de R$%.2f'%prestação)
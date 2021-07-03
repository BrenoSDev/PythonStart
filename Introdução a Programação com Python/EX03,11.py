preço = float(input('Digite o preço da mercadoria: R$'))
desconto = int(input('Porcentagem de desconto: '))
novo_preço = (100 - desconto)*preço / 100
print('Após um desconto de %d porcento, o novo preço da mercadoria é R$%.2f!'%(desconto, novo_preço))
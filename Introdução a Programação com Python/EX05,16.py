#Utilizando o contador de cédulas com os valores 501, 745, 384, 2, 7, 1
compra = int(input('Digite o valor total da compra: '))
cédulas = 0
nota = 50
total_a_pagar = compra
while True:
    if nota <= total_a_pagar:
        total_a_pagar -= nota
        cédulas += 1
    else:
        print('%d células de R$%d'%(cédulas, nota))
        if total_a_pagar == 0:
            break
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        cédulas = 0
#Caixa eletrônico com notas e moedas
def arredondar(num):    
    return float('%g' % (num))
compra = float(input('Digite o total da compra: R$'))
cédulas = 0
nota = 100
total_a_pagar = compra
while True:
    if nota <= total_a_pagar:
        total_a_pagar -= nota
        cédulas += 1
        total_a_pagar = arredondar(total_a_pagar)
    else:
        if nota >= 1:
            print('%d nota(s) de R$%.2f'%(cédulas, nota))
        else:
            print('%d moeda(s) de R$%.2f'%(cédulas, nota))
        if total_a_pagar == 0:
            break
        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        elif nota == 1:
            nota = 0.5
        elif nota == 0.5:
            nota = 0.1 
        elif nota == 0.1:
            nota = 0.05
        elif nota == 0.05:
            nota = 0.02
        elif nota == 0.02:
            nota = 0.01
        cédulas = 0
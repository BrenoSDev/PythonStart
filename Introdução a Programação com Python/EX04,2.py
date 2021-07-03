#Multa por excesso de velocidade
v = float(input('Velocidade do carro em km/h: '))
if v > 80:
    multa = (v - 80)*5
    print('Você foi multado e terá que pagar uma multa de R$%.2f'%multa)
if v <= 80:
    print('Parabéns! Continue respeitando os limites de velocidade da rodovia!')
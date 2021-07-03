distância = float(input('Distância da viagem em km: '))
velocidade = float(input('Digite a velocidade média em km/h: '))
tempo = distância/velocidade
print('Dirigindo a %.1f km/h, sua viagem durará %.2f horas'%(velocidade, tempo))
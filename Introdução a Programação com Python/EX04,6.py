distância = float(input('Qual distância você deseja percorrer em km: '))
if distância > 200:
	taxa = 0.45
else:
    taxa = 0.50
valor = distância * taxa
print('Para uma viagem de %.1f km, o valor da passagem será de R$%.2f.'%(distância, valor))
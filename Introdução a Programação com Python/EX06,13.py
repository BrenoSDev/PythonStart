#Temperatura máxima, mínima e média de Mons, Bélgica
T = [-10,-8,0,1,2,5,-2,-4]
máxima = mínima = T[0]
soma = 0
for t in T:
	if t > máxima:
		máxima = t
	if t < mínima:
		mínima = t
	soma += t
print('A temperatura máxima foi de %d ºC, a mínima foi de %d ºC!'%(máxima, mínima))
print('A média das temperaturas foi %.2f ºC'%(soma/len(T)))
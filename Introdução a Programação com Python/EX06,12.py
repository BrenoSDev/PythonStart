#Menor elemento de uma lista
L=[1,7,-2,4]
mínimo=L[0]
for v in L:
	if v < mínimo:
		mínimo = v
print(mínimo)
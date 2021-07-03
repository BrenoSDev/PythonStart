#Impressão de tabuadas
tabuada = 1
while tabuada <= 10:
	número = 1
	while número <= 10:
		print('%d x %d = %d'%(tabuada, número, tabuada*número))
		número += 1
	tabuada += 1

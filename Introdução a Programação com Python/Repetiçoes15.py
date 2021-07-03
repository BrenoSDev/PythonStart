#Impressão de tabuadas sem repetições aninhadas
tabuada = 1
número = 1
while tabuada <= 10:
	print('%d x %d = %d' %(tabuada, número, tabuada*número))
	número += 1
	if número == 11:
		número = 1
		tabuada += 1
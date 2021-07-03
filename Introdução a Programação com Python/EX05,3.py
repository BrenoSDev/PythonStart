#Contagem regressiva do lançamento de um foguete
import time
x = 10
while x >= 0:
	print(x)
	x -= 1
	time.sleep(1)
print('Fogo!!!')
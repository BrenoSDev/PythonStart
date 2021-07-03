#Imprimindo números ímpares até um limite digitado pelo usuário
import time
limite = int(input('Digite o último número ímpar a imprimir: '))
x = 1
while x <= limite:
    print(x)
    time.sleep(0.1)
    x += 2
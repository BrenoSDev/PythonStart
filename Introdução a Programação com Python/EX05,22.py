#Impressão de tabuada com menu
from time import sleep
print('Bem vindo a tabuada virtual! Escolha uma operação e a tabuada completa dessa operação aparecerá na tela!')
while True:
    menu = ''
    while menu != 'SOMA' and menu != 'SUBTRAÇÃO' and menu != 'SAIR' and menu != 'DIVISÃO' and menu != 'MULTIPLICAÇÃO':
        menu = input('Operação(Multiplicação, Divisão, Soma, Subtração ou Sair): ').upper()
    if menu == 'SAIR':
        break
    tabuada = 1
    while tabuada <= 10:
        número = 1
        while número <= 10:
            if menu == 'MULTIPLICAÇÃO':
                print('%d x %d = %d'%(número, tabuada, número*tabuada))
            elif menu == 'DIVISÃO':
                print('%d / %d = %d' %(número*tabuada, tabuada, número*tabuada/tabuada))
            elif menu == 'SOMA':
                print('%d + %d = %d' %(número, tabuada, número+tabuada))
            elif menu == 'SUBTRAÇÃO':
                print('%d - %d = %d'%(número, tabuada, número - tabuada))
            sleep(0.2)
            número += 1
        tabuada += 1
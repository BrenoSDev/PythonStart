#Tabuada v2
import time
print('Seja bem vindo a tabuada virtual! Digite um valor e a tabuada de multiplicar irá aparecer na tela!')
while True:
    n = ' '
    while n.isdigit() == False:
        n = input('Tabuada de: ')
    n = int(n)
    início = ' '
    while início.isdigit() == False:
        início = input('Por qual número você deseja multiplicar primeiro: ')
    início = int(início)
    fim = ' '
    while fim.isdigit() == False:
        fim = input('Por qual número você deseja multiplicar por último: ')
    fim = int(fim)
    while início <= fim:
        print('%d x %d = %d'%(n, início, n*início))
        time.sleep(0.5)
        início += 1
    continuar = ' '
    while continuar[0] != 'S' and continuar[0] != 'N':
        continuar = input('Você quer continuar(S/N)? ').upper()
        if len(continuar) == 0:
            continuar = ' '
    if continuar[0] == 'N':
        break
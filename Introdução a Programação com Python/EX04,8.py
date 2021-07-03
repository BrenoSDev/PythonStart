n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor: '))
operação = input('Qual operação você deseja realizar (+, -, *, /): ')
if operação == '+':
    resultado = n1 + n2
elif operação == '-':
    resultado = n1 - n2
elif operação == '*':
    resultado = n1 * n2
elif operação == '/':
    resultado = n1 / n2
else:
    print('Operação inválida! Digite + para soma, - para subtração, * para multiplicação ou / para divisão.')
    resultado = 0
print('%d %s %d = %.1f'%(n1, operação, n2, resultado))
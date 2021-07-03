#Simulação de um banco com duas filas
último1 = último2 = 10
fila1 = list(range(1, último1+1))
fila2 = list(range(1, último2+1))
while True:
    print('\nExistem %d clientes na fila 1'%len(fila1))
    print('Fila 1:', fila1)
    print('\nExistem %d clientes na fila 2'%len(fila2))
    print('Fila 2:', fila2)
    print('\nDigite F para adicionar um cliente ao fim da fila 1 e G ao fim da fila 2')
    print('ou A para atendimento na fila 1 e B para atendimento na fila 2. S para sair.')
    print('VCocê também pode fazer múltiplas operações como FABG ou FFAAGG!')
    operação = input('Operação (A, B, F, G ou S): ')
    if len(operação) == 0:
        operação = ' '
    c = 0
    while c < len(operação):
        if operação[c] == 'A':
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print('O cliente %d da fila 1 foi atendido!'%atendido)
            else:
                print('Fila 1 vazia! Ninguém para atender!')
        elif operação[c] == 'B':
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print('O cliente %d da fila 2 foi atendido!'%atendido)
            else:
                print('Fila 2 vazia! Ninguém para atender!')
        elif operação[c] == 'F':
            último1 += 1
            fila1.append(último1)
        elif operação[c] == 'G':
            último2 += 1
            fila2.append(último2)
        elif operação[c] == 'S':
            break
        else:
            print('Operação Inválida! Digite apenas F, G, A, B ou S!')
        c += 1
    if 'S' in operação:
        break
print('Fila 1:', fila1)
print('Fila 2:', fila2)
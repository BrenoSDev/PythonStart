#Simulação de uma fila de banco com múltiplos comandos
último = 10
fila = list(range(1, último+1))
while True:	
    print('\nExistem %d clientes na fila'%len(fila))
    print('Fila atual:', fila)
    print('Digite F para adicionar um cliente ao fim da fila, ')
    print('ou A para realizar o atendimento. S para sair.')
    print('Você também pode realizar operações múltiplas como FFFF ou FAFA!')
    operação = input('Operação (F, A ou S): ')
    c = 0
    if len(operação) == 0:
        operação = ' '
    while c < len(operação):
        if operação[c] == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print('Cliente %d atendido'%atendido)
            else:
                print('Fila vazia! Ninguém para atender')
        elif operação[c] == 'F':
            último += 1
            fila.append(último)
        elif operação[c] == 'S':
            break
        else:  
            print('Operação inválida! Digite apenas F, A ou S!')
        c += 1
    if 'S' in operação:
        break
print('Fila:', fila)
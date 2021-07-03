#Leitura de duas listas e armazenamento delas em uma terceira
def isnumber(num):
    try:
        float(num)
    except ValueError:
        return False
    return True
print('Organizador de arquivos! Digite valores e nós os organizaremos em uma lista!')
L1 = []
L2 = []
print('Lista 1:')
while True:
    informação = input('Digite um valor numérico,palavra ou frase(Digite SAIR para terminar a lista): ')
    if informação == 'SAIR':
        break
    if isnumber(informação) == True:
        L1.append(float(informação))
    else:
        L1.append(informação)
print('Lista 2:')
while True:
    informação = input('Digite um valor numérico, palavra ou frase(Digite SAIR para terminar a lista): ')
    if informação == 'SAIR':
        break
    if isnumber(informação) == True:
        L2.append(float(informação))
    else:
        L2.append(informação)
dados = []
dados.append(L1)
dados.append(L2)
print('Dados digitados:\n{}\n{}'.format(dados[0], dados[1]))
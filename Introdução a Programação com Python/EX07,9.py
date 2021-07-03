#Jogo da Forca com lista de palavras
lista_palavras = ['biscoito', 'pastel', 'parar', 'linha', 'poderoso', 'ansiedade']
número = int(input('Digite um valor: '))
indice = (número * 776) % len(lista_palavras)
palavra = lista_palavras[indice]
for x in range(100):
	print()
digitadas = []
acertos = []
erros = 0
while True:	
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print('Você acertou!')
        break
    tentativa = input('\nDigite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já tentou esta letra!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    linha1 = list('X==:==\nX  :  ')
    print(''.join(linha1))
    linha2 = list('X  O  ') if erros >= 1 else list('X')
    print(''.join(linha2))
    linha3 = [' ', ' ', ' ', ' ', ' ']
    if erros == 2:
        linha3[2] = '|'
    elif erros == 3:
        linha3[2] = '|'
        linha3[1] = '\\'
    elif erros >= 4:
        linha3[2] = '|'
        linha3[1] = '\\'
        linha3[3] = "/"
    print('X%s' %''.join(linha3))
    linha4 = [' ', ' ', ' ', ' ', ' ']
    if erros == 5:
        linha4[1] = '/'
    elif erros >= 6:
        linha4[1] = '/'
        linha4[3] = '\\'
    print('X%s'%''.join(linha4))
    linha_final = list('X\n===========')
    print(''.join(linha_final))
    if erros == 6:
        print('Enforcado!')
        print('A palavra secreta era: {}'.format(palavra))
        break
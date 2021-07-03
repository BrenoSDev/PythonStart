#Programa que lê três strings e imprime o resultado da substituição da primeira, dos caracteres da segunda pelos da terceira
print('Digite três strings e nós substituiremos os caracteres da segunda pelos da terceira na primeira!')
string1 = list(input('String 1: '))
string2 = '   '
string3 = ''
while len(string2) != len(string3):
    print('As string 2 e 3 devem conter o mesmo número de letras!')
    string2 = list(input('String 2: '))
    string3 = list(input('String 3: '))
resultado = string1[:]
contador = 0
for letra in string2:
    while letra in resultado:
        posicao = resultado.index(letra)
        resultado[posicao] = string3[contador]
    contador += 1
print('Resultado: %s'%(''.join(resultado)))
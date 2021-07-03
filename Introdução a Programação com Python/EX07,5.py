#Gerando string a partir de outras duas strings, com os caracteres da segunda retirados da primeira
print('Escreva duas strings e nós geraremos uma terceira com os caracteres da segunda retirados da primeira!')
string1 = list(input('String 1: '))
string2 = list(input('String 2: '))
string3 = []
for c in string1:
    if c not in string2:
        string3.append(c)
print('\n1º String: %s\n2º String: %s\n3º String: %s'%(''.join(string1), ''.join(string2), ''.join(string3)))
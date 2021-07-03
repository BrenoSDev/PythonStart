#Gerador de string com caracteres em comum de duas outras strings
print('Digite 2 strings e nós geraremos uma terceira com os caracteres em comum!')
string1 = input('String 1: ')
string2 = input('String 2: ')
string3 = []
lista_caractere = list(string2)
for c in lista_caractere:
    if c in string1:
        string3.append(c)
print('Os caracteres em comum entre as duas strings são: {}'.format(''.join(string3)))
#Criador de string com caracteres únicos a partir de duas strings
print('Digite 2 strings e uma terceira será criada apenas com os caracteres que não são comuns as duas!')
string1 = input('String 1: ')
string2 = input('String 2: ')
string3 = []
list(string1)
list(string2)
for c in string1:
    if c not in string2:
        string3.append(c)
for d in string2:
    if d not in string1:
        string3.append(d)
print('\nString 1: %s\nString2: %s\nCaracteres únicos: %s'%(''.join(string1), ''.join(string2), ''.join(string3)))
#Escrevendo quantos caracteres de cada tipo há em uma string
print('Digite uma string e nós mostraremos quantas vezes aparece cada caractere!')
string = list(input("String: "))
caracteres = []
for c in string:
    if c not in caracteres:
        print('%1s: %dx'%(c, string.count(c)))
        caracteres.append(c)

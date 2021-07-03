#Verificador de strings
print('Digite 2 strings e nós verificaremos se a segunda pode ser encontrada na primeira!')
string1 = input('Digite uma frase: ')
string2 = input('Digite outra frase: ')
encontrou = string1.upper().find(string2.upper())
if encontrou >= 0:
    print(f'{string2} encontrado na posição {encontrou} de {string1}')
else:
    print(f'{string2} não foi encontrado!')
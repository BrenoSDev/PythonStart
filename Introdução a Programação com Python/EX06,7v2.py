#Verificador de parênteses V2
print('Digite uma expressão com parênteses e nós verificaremos se eles foram abertos e fechados corretamente!')
expressão = input('Expressão: ')
lista_parênteses = []
c = 0
while c < len(expressão):
    if expressão[c] == '(':
        lista_parênteses.append(expressão[c])
        print(expressão[c], end='')
    elif expressão[c] == ')':
        if len(lista_parênteses) > 0:
            lista_parênteses.pop(-1)
        else:
            lista_parênteses.append(expressão[c])
        print(expressão[c], end='')
    c += 1
if len(lista_parênteses) == 0:
    print(' OK')
else: 
    print(' ERRO')
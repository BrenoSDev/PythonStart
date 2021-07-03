#Verificador de parênteses
print('Digite uma expressão usando parênteses e nós verificaremos se você os abriu e fechou na ordem correta!')
expressão = input('Expressão: ')
lista_parênteses = []
c = 0
while c < len(expressão):
    if expressão[c] == '(' or expressão[c] == ')':
        lista_parênteses.append(expressão[c])
    c += 1
c = aberto = fechado = 0
while len(lista_parênteses) > 0:
    retirado = lista_parênteses.pop(-1)
    if retirado == '(':
        aberto += 1
    elif retirado == ')':
        fechado += 1
if aberto == fechado:
    print('Você abriu  e fechou todos os parênteses corretamente!')
elif aberto > fechado:
    print('Você esqueceu de fechar %d parênteses'%(aberto-fechado))
else:
    print('Você esqueceu de abrir %d parênteses'%(fechado-aberto))

#Multiplicação de dois números usando adição
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('%d x %d = '%(n1, n2), end='')
c = 1
while c < n2:
    print('%d + '%(n1), end='')
    c += 1
print('%d = '%n1, end='')
c = 1
produto = n2
while c < n1:
    print('%d + '%(n2), end='')
    c += 1
    produto += n2
print('%d = %d'%(n2, produto))
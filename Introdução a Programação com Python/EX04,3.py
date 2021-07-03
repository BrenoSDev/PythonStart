n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um segundo valor: '))
n3 = float(input('Digite um último valor: '))
maior = n1
menor = n1
if n2 > maior or n3 > maior:
    if n2 > n3:
        maior = n2
    if n3 > n2:
        maior = n3
if n2 < menor or n3 < menor:
    if n2 < n3:
        menor = n2
    if n3 < n2:
        menor = n3
print('O maior dos valores digitados foi %.1f e o menor foi %.1f'%(maior, menor))
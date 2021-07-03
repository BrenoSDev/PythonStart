#Verificador de números palíndromos
print('Digite um valor e nós verificaremos se ele é um palíndromo ou não!')
n = input('Digite um valor: ')
while n.isdigit() == False or len(n) < 2:
    print('\033[31mERRO! Digite apenas números inteiros, positivos e com mais de dois dígitos!\033[m')
    n = input('Digite um valor: ')
tamanho = len(n)
igual = c = 0
while c < tamanho:
    if n[c] == n[tamanho - c -1]:
        igual += 1
    c += 1
if igual == tamanho:
    print('O número %s é um palíndromo!'%n)
else:
    print('O número %s não é um palíndromo!'%n)
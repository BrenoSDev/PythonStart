#Formatação de números decimais
print('{:f}'.format(1579.543))
print('{:n}'.format(1579.543))
import locale
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')
print('{:n}'.format(1579.543))
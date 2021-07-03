#O formato d e o formato n
print('{:d}'.format(5678))
print('{:n}'.format(5678))
import locale
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')
print('{:n}'.format(5678))
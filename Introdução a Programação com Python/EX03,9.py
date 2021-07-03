# Converter tempo em segundos
dias = int(input('Número de dias: '))
horas = int(input('Número de horas: '))
minutos = int(input('Número de minutos: '))
segundos = int(input('Número de segundos: '))
tempo = ((dias*24 + horas)*60 + minutos)*60 + segundos
print('Esse valor equivale a %d segundos'%tempo)
#Redução de vida de um fumante
cigarros = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos = int(input('Há quantos anos você fuma? '))
redução_de_vida = ((anos*365*cigarros)*10)/(24*60)
print('Seu estilo de vida fará você perder %d dias de vida!'%redução_de_vida)
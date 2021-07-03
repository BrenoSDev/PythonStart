matéria1 = float(input('Digite a sua nota na matéria 1: '))
matéria2 = float(input('Digite a sua nota na matéria 2: '))
matéria3 = float(input('Digite a sua nota na matéria 3: '))
aprovado = matéria1 >= 7 and matéria2 >= 7 and matéria3 >= 7
if aprovado == True:
	print('Parabéns! Você foi aprovado.')
else:
	print('Que pena! Você foi reprovado!')
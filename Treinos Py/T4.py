#Validação de dados com nota de aluno
def isnumber(value):
    try:
        float(value)
    except ValueError:
        return False
    return True
    
nota = input('Digite sua nota da unidade de 0 a 10: ')
while isnumber(nota) == False or isnumber(nota) == True and (float(nota) < 0 or float(nota) > 10):
	print('Valor incorreto!')
	nota = input('Digite sua nota da unidade de 0 a 10: ')
print('Sua nota foi %.1f'%float(nota))

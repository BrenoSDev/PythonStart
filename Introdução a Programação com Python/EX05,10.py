#Contagem de respostas corretas com alternativas maiúsculas ou minúsculas
pontos = 0
questão = 1
while questão <= 3:
	resposta = input('Resposta da questão %d: '%questão)
	if questão == 1 and (resposta == 'b' or resposta == 'B'):
		pontos += 1
	if questão == 2 and (resposta == 'a' or resposta == 'A'):
		pontos += 1
	if questão == 3 and (resposta == 'd' or resposta == 'D'):
		pontos += 1
	questão += 1
print('O aluno fez %d ponto(s).'%pontos)
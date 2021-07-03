#Validação simples de usuário e senha
usuário = input('Nome de usuário: ')
senha = input('Senha: ')
while usuário == senha:
	print('Dados incorretos! O nome de usuário não pode ser igual a senha!')
	senha = input('Senha: ')
print('Dados cadastrados com sucesso!')
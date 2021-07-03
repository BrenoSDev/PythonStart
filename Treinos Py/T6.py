#Validação de informações
nome = input('Nome: ')
while len(nome) <= 3:
	print('\033[31mERRO! O nome deve possuir mais de 3 caracteres!\033[m')
	nome = input('Nome: ')
idade = input('Idade: ')
while int(idade) < 0 or int(idade) > 150:
    print('\033[31mERRO! Digite uma idade entre 0 e 150 anos:\033[m')
    idade = input('Idade: ')
salário = input('Salário: ')
while float(salário) < 0:
    print('\033[31mERRO! O salário não pode ser negativo!\033[m')
    salário = input('Salário: ')
sexo = input('Sexo(M/F): ').upper()
while sexo[0] != 'M' and sexo[0] != 'F':
    print('\033[31mERRO! Digite apenas M ou F no sexo!\033[m')
    sexo = input('Sexo(M/F): ').upper()
estado_civil = input('Estado civil(S/C/V/D): ').upper()
while estado_civil[0] != 'S' and estado_civil[0] != 'C' and estado_civil[0] != 'V' and estado_civil[0] != 'D':
    print('\033[31mERRO! Digite um estado civil válido!\033[m')
    estado_civil = input('Estado civil(S/C/V/D): ').upper()
print('Dados cadastrados com sucesso!')
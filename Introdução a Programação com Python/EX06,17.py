#Exemplo de dicionário com estoque, operações de venda e entrada do usuário
estoque={"tomate":[1000,2.30],
		 "alface":[ 500,0.45],
		 "batata":[2001,1.20],
		 "feijão":[100, 1.50]}
def mostrar_estoque():
    print('Estoque: \n')
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Estoque: ", dados[0])
        print("Preço: %.2f\n"%dados[1])
mostrar_estoque()
total=0
while True:
    produto=input("Digite o produto que você deseja comprar (fim para sair): ")
    if produto == "fim":
        break
    if produto not in estoque.keys():
        print('\033[1;31mPRODUTO NÃO ENCONTRADO!\033[m')
    else:
        quantidade = int(input('Quantidade: '))
        if quantidade < 0:
            print('\033[1;31mERRO! QUANTIDADE INEXISTENTE!\033[m')
        elif quantidade > estoque[produto][0]:
            print('\033[1;31mERRO! QUANTIDADE INSUFICIENTE NO ESTOQUE!\033[m')
        else:
            custo = quantidade*estoque[produto][1]
            print('%12s: %3d x %6.2f = %6.2f'%(produto, quantidade, estoque[produto][1], custo))
            estoque[produto][0] -= quantidade
            total += custo
print(' Custo total: %21.2f\n'%total)
mostrar_estoque()
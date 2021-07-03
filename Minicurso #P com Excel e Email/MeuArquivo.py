import pandas as pd
import win32com.client as win32

#Importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

#Visualizar a base de dados
pd.set_option('display.max_columns', None) #Opção, Valor
print(tabela_vendas)

#Faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

#Quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

#Ticked medio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0:'Ticket Médio'})
print(ticket_medio)

#Enviar um email com um relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To='brenoruan18@gmail.com'
mail.Subject='Relatório de Vendas por Loja'
mail.HTMLBody=f'''
<p>Prezados</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final':'R${:,.2f}'.format})}

<p>Quantidade vendida:</p>
{quantidade.to_html()}

<p>Ticket medio dos produtos em cada loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio':'R${:,.2f}'.format})}

<p>Qualquer dúvida estou a disposição.</p>

<p>Att.</p>
<p>Breno</p>
'''

mail.Send()
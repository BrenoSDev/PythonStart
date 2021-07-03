#Importando o mysql.connector
import mysql.connector

#Criando conexão com banco de dados
"""con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='bre123no456')"""

#Se conectando a banco de dados já existente
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='bre123no456',
    database='mydatabase'
)
    
#Criando banco de dados
mycursor = con.cursor()
"""mycursor.execute("create database mydatabase")"""

#Verificando a existência de banco de dados no sistema
"""mycursor.execute("show databases;")
for x in mycursor:
    print(x)"""


#Criando tabela
"""mycursor.execute('create table clientes (nome varchar(255), endereco varchar(255));')"""

#Verificando se a tabela foi criada
mycursor.execute('show tables;')
for tabela in mycursor:
    print(tabela)

#Criando tabela com chave primária
"""mycursor.execute("create table clientes (id int auto_increment primary key, nome varchar(255),endereço varchar(255));")"""

#Criando chave primária em tabela já existente
"""mycursor.execute('alter table clientes add column id int auto_increment primary key;')"""

#Inserindo dados
"""sql = 'insert into clientes (nome, endereco) values (%s, %s);'
val = ('John', 'Highway 21')
mycursor.execute(sql, val)

con.commit() #Garante que a alteração será feita na tabela

print(mycursor.rowcount, "dado inserido.")"""

#Inserindo várias linhas com o método executemany()
#O segundo parâmetro desse método é uma lista de tuplas com os dados que você deseja inserir
"""sql = 'insert into clientes (nome, endereco) values (%s, %s);'
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Vale 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 254'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'SideWay 1633')
    ]
mycursor.executemany(sql, val)

con.commit()

print(mycursor.rowcount, 'foi inserido')"""

#Inserindo uma linha e retornando o id
"""sql = 'insert into clientes (nome, endereco) values (%s, %s);'
val = ('Michelle', 'Blue Village')
mycursor.execute(sql, val)
con.commit()
print('1 dado inserido, ID: ', mycursor.lastrowid)"""

#Selecionando registros da tabela
"""mycursor.execute("select * from clientes;")
myresult = mycursor.fetchall() #O método fetchall() busca todas as linhas da última instrução executada
for x in myresult:
    print(x)"""
    
#Selecionando algumas colunas
"""mycursor.execute("select nome, endereco from clientes;")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)"""


#Se você estiver interessado em apenas uma linha pode usar o método fetchone() que retornará a primeira linha do resultado
"""mycursor.execute('select * from clientes;')
myresult = mycursor.fetchone()
print('\n', myresult)"""

#Selecionando registros com um filtro
"""sql = "select * from clientes where endereco='Highway 21'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)"""
    
#Usando caracteres curinga %
"""sql = "select * from clientes where endereco like '%way%';"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)"""
    
#Impedir injeção de SQL
#Escapando dos valores de consulta usando o método placholder %s
"""sql = "select * from clientes where endereco = %s;"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)"""
    
#ORDER BY
"""sql = "select * from clientes order by nome;"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('')"""
#ORDER BY DESC
"""sql = "select * from clientes order by nome desc;"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)"""
    
#Apagando registros
"""sql = "delete from clientes where endereco = 'Mountain 21';"
mycursor.execute(sql)
con.commit() #Comando necessário para fazer as alterações na tabela
print(mycursor.rowcount, "dado(s) deletados.")"""

#Impedindo injeção de sql
"""sql = "delete from clientes where endereco = %s;"
adr = ("Yellow Garden 2",)
mycursor.execute(sql,adr)
con.commit()
print(mycursor.rowcount, "dado(s) deletados!")"""

#Apagar uma tabela
"""sql = "drop table clientes;"
mycursor.execute(sql)"""

#Apagando apenas se existir
"""sql = "drop table if exists clientes;"
mycursor.execute(sql)"""

#Atualizando registros
"""sql = "update clientes set endereco = 'Canyon 123' where endereco = 'Valley 345';"
mycursor.execute(sql)
con.commit()
print(mycursor.rowcount, "linhas afetadas")"""

#Limitando o resultado
mycursor.execute("select * from clientes limit 5;")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
cursor = db_connection.cursor() # Cria uma variável cursor que fica com o retorno da execução da query
nome = input("Digite seu nome: ") # Usuário digita o nome
cursor.execute(f"INSERT INTO Cliente(nome,cpf,saldo) VALUES ('{nome}','45678912399',0)") # Deixamos a query que salva no banco de dados pronta pra ser chamada
db_connection.commit() # Enviamos todas as querys prontas pra o banco
print(cursor) # Printa o retorno do resultado da query
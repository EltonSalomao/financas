import mysql.connector
from mysql.connector import errorcode


def cadastrar_cliente():
    nome=input("Digite o seu nome: ")
    cpf=input("Digite o seu cpf: ")
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(f"INSERT INTO Cliente(nome,cpf,saldo) VALUES ('{nome}',{cpf},0)") # Deixamos a query que salva no banco de dados pronta pra ser chamada
    db_connection.commit() # Enviamos todas as querys prontas pra o banco
    db_connection.close()



def listar_cliente():
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT * from Cliente") # Deixamos a query que salva no banco de dados pronta pra ser chamada
    resultado=cursor.fetchall()
    for cliente in resultado:
        print(cliente)
    db_connection.close()

listar_cliente()


# teste
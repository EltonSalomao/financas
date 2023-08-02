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

def deletar_cliente():
    listar_cliente()
    id = int(input("Digite o ID."))
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(f"DELETE from Cliente WHERE id_cliente={id}") # Deixamos a query que salva no banco de dados pronta pra ser chamada
    


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

cadastrar_cliente()

def menu_geral():
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    print("1 - Menu Cliente")
    print("2 - Menu Lançamento")
    print("3 - Menu Categoria")
    try:
        op=input("Digite dentre as opções a seguir: ")
        if op==1:
            print("1 - Cadastrar Cliente")
            print("2 - Deletar Cliente")
            print("3 - Listar Cliente")
    except:
        print("Digite uma opção válida!")


    db_connection.close()



# teste
# teste 2

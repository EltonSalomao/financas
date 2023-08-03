import mysql.connector
from mysql.connector import errorcode


def cadastrar_cliente():
    nome=input("Digite o seu nome: ")
    cpf=input("Digite o seu cpf: ")
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(f"INSERT INTO Cliente(nome,cpf,saldo) VALUES ('{nome}','{cpf}',0)") # Deixamos a query que salva no banco de dados pronta pra ser chamada
    db_connection.commit() # Enviamos todas as querys prontas pra o banco
    db_connection.close()

def deletar_cliente():
    listar_cliente()
    id = int(input("Digite o ID do Cliente a ser deletado: "))
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

def listar_lançamento():
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT * from Lancamento") # Deixamos a query que salva no banco de dados pronta pra ser chamada
    resultado=cursor.fetchall()
    for lançamento in resultado:
        print(lançamento)
    db_connection.close()

def deletar_lançamento():
    listar_lançamento()
    id = int(input("Digite o ID do lançamento a ser excluído: "))
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(f"DELETE from Lancamento WHERE id_lancamento={id}") # Deixamos a query que salva no banco de dados pronta pra ser chamada
    db_connection.commit() # Enviamos todas as querys prontas pra o banco
    db_connection.close()

def cadastrar_categoria():
    nome=input("Digite o nome da categoria: ")
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(f"INSERT INTO Categoria(nome) VALUES ('{nome}')") # Deixamos a query que salva no banco de dados pronta pra ser chamada
    db_connection.commit() # Enviamos todas as querys prontas pra o banco
    db_connection.close()

def listar_categorias():
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT * from Categoria") # Deixamos a query que salva no banco de dados pronta pra ser chamada
    resultado=cursor.fetchall()
    for categoria in resultado:
        print(categoria)
    db_connection.close()

def deletar_categoria():
    listar_categorias()
    id_categoria=int(input("Digite o ID da categoria a ser deletada: "))
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(f"DELETE from Categoria WHERE id_categoria={id_categoria}") # Deixamos a query que salva no banco de dados pronta pra ser chamada
    db_connection.commit() # Enviamos todas as querys prontas pra o banco
    db_connection.close()

def menu_geral():
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    print("1 - Menu Cliente")
    print("2 - Menu Lançamento")
    print("3 - Menu Categoria")
    try:
        op=input("Digite dentre as opções a seguir: ")
        if op=="1":
            print("1 - Cadastrar Cliente")
            print("2 - Deletar Cliente")
            print("3 - Listar Cliente")
            opcli=input("Digite a opção que você deseja: ")
            if opcli=="1":
                cadastrar_cliente()
            elif opcli=="2":
                deletar_cliente()
            elif opcli=="3":
                listar_cliente()

        elif op=="2":
            print("1 - Cadastrar Lançamento")
            print("2 - Deletar Lançamento")
            print("3 - Listar Lançamentos")
            oplan=input("Digite a opção desejada: ")
            if oplan=="1":

            elif oplan=="2":
                deletar_lançamento()
            elif oplan=="3":
                listar_lançamento()
        elif op=="3":
            print("1 - Cadastrar Categoria")
            print("2 - Deletar Categoria")
            print("3 - Listar Categorias")
            opcat=input("Digite a opção desejada: ")
            if opcat=="1":
                cadastrar_categoria()
            elif opcat=="2":
                deletar_categoria()
            elif opcat=="3":
                listar_categorias()
    except:
        print("Digite uma opção válida!")


    db_connection.close()


deletar_categoria()

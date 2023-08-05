import mysql.connector
from mysql.connector import errorcode

def inserir_deletar(query_sql):
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(query_sql) # Deixamos a query que salva no banco de dados pronta pra ser chamada
    db_connection.commit() # Enviamos todas as querys prontas pra o banco
    db_connection.close()

def consultar(query_sql):
    db_connection = mysql.connector.connect(host='192.168.188.165', port='3306', user='admin', password='admin', database='financias') # Abrindo conexão com o banco de dados
    cursor = db_connection.cursor()
    cursor.execute(query_sql) # Deixamos a query que salva no banco de dados pronta pra ser chamada
    resultado=cursor.fetchall()
    db_connection.close()
    return resultado

def cadastrar_cliente():
    nome=input("Digite o seu nome: ")
    cpf=input("Digite o seu cpf: ")
    inserir_deletar(f"INSERT INTO Cliente(nome,cpf,saldo) VALUES ('{nome}','{cpf}',0)")
    print(f"Cliente {nome} cadastrado com sucesso.")

def deletar_cliente():
    listar_cliente()
    id = int(input("Digite o ID do Cliente a ser deletado: "))
    inserir_deletar(f"DELETE from Cliente WHERE id_cliente={id}")
    print(f"Cliente_{id} deletado com sucesso.")


def listar_cliente():
    clientes = consultar(f"SELECT * from Cliente")
    for cliente in clientes:
        print(cliente)

def cadastrar_lancamento():
    listar_cliente()
    descricao=(input("Digite a descrição do valor lançado: "))
    valor=float(input("Digite o valor a ser lançado: "))
    print("1 - Receita")
    print("2 - Despesa")
    tipo=input("Digite a opção desejada: ")
    if tipo=="2":
        valor *= -1
    data_lancamento=(input("Digite a data que você está lançando:"))
    id_cliente=int(input("Informe sobre o seu ID: "))
    id_categoria=int(input("Informe o ID da categoria: "))
    inserir_deletar(f"INSERT INTO lancamento (data_lancamento, valor, descricao, id_cliente, id_categoria) VALUES ('{data_lancamento}', {valor}, '{descricao}', {id_cliente}, {id_categoria}) ")
    print(f"Lançamento {descricao} cadastrado com sucesso.")

def listar_lançamento():
    clientes = consultar(f"SELECT * from Lancamento")
    for cliente in clientes:
        print(cliente)

def deletar_lançamento():
    listar_lançamento()
    id = int(input("Digite o ID do lançamento a ser excluído: "))
    inserir_deletar(f"DELETE from Lancamento WHERE id_lancamento={id}")
    print(f"Lançamento {id} deletado com sucesso.")

def cadastrar_categoria():
    nome=input("Digite o nome da categoria: ")
    inserir_deletar(f"INSERT INTO Categoria(nome) VALUES ('{nome}')")
    print(f"Categoria {nome} cadastrada com sucesso.")

def listar_categorias():
    clientes = consultar(f"SELECT * from Categoria")
    for cliente in clientes:
        print(cliente)

def deletar_categoria():
    listar_categorias()
    id_categoria=int(input("Digite o ID da categoria a ser deletada: "))
    inserir_deletar(f"DELETE from Categoria WHERE id_categoria={id_categoria}")
    print(f"Categoria {id_categoria} deletada com sucesso.")

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
                cadastrar_lancamento()
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


menu_geral()

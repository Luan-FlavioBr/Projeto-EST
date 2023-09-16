import sqlite3 as sql

def retornar_tables():
    banco = sql.connect("banco_cadastro.db")
    cursor = banco.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")

    tabelas = cursor.fetchall()

    lista = [nome[0] for nome in tabelas]
    banco.commit()
    banco.close()
    
    return lista


def cadastrar_usuario(login, senha):
    banco = sql.connect("banco_cadastro.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (login TEXT PRIMARY KEY, password TEXT)")

    cursor.execute(f"INSERT INTO usuarios VALUES('{login}', '{senha}')")

    banco.commit()
    banco.close()


def verificar_cadastro(login):
    banco = sql.connect("banco_cadastro.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (login TEXT PRIMARY KEY, password TEXT)")

    cursor.execute(f"SELECT * FROM usuarios WHERE login = '{login}'")
    login_dados = cursor.fetchall()
    banco.close()

    return login_dados


def inserir_rol_dados_qualitativos(lista, nome_table):
    banco = sql.connect('banco_cadastro.db')
    cursor = banco.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_table} (id INTEGER PRIMARY KEY AUTOINCREMENT, dado TEXT)")

    for dado in lista:
        dado = str(dado)
        if not any(char.isdigit() for char in dado):
            cursor.execute(f"INSERT INTO {nome_table} (dado) VALUES ('{dado}')")
        else:
            print("DADO INVÁLIDO!")
            banco.rollback()
            banco.close()
            return None
    banco.commit()
    banco.close()


def buscar_rol_dados(nome_table):
    lista_de_dados = []
    banco = sql.connect('banco_cadastro.db')
    cursor = banco.cursor()
    
    cursor.execute(f"SELECT * FROM {nome_table}")
    
    while True:
        dado = cursor.fetchone()
        if dado != None:
            lista_de_dados.append(dado[1])
        else:
            break
    banco.commit()
    banco.close()
    return lista_de_dados

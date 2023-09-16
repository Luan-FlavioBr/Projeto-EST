import sqlite3 as sql


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



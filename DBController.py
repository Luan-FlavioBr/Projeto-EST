import sqlite3 as sql

def retornar_tables():
    banco = sql.connect("banco_cadastro.db")
    cursor = banco.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")

    tabelas = cursor.fetchall()

    lista = []
    for nome in tabelas:
        if nome[0] != "usuarios":
            lista.append(nome[0])

    banco.close()
    
    return lista


def retornar_tables_pareto():
    banco = sql.connect("banco_cadastro.db")
    cursor = banco.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")

    tabelas = cursor.fetchall()

    lista = list()
    for tabela in tabelas:
        tabela = tabela[0]
        if tabela != 'usuarios' and "_1" not in tabela:
            lista.append(tabela[:-2])

    banco.close()
    
    return lista


def retornar_tables_histograma():
    banco = sql.connect("banco_cadastro.db")
    cursor = banco.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")

    tabelas = cursor.fetchall()

    lista = list()
    for tabela in tabelas:
        tabela = tabela[0]
        if tabela != 'usuarios' and "_2" not in tabela and "_3" not in tabela:
            lista.append(tabela[:-2])

    banco.close()
    
    return lista


def cadastrar_usuario(login, senha):
    banco = sql.connect("banco_cadastro.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (login TEXT PRIMARY KEY, password TEXT)")

    cursor.execute(f"INSERT INTO usuarios VALUES(?, ?)", (login, senha))

    banco.commit()
    banco.close()


def verificar_cadastro(login):
    banco = sql.connect("banco_cadastro.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (login TEXT PRIMARY KEY, password TEXT)")

    cursor.execute(f"SELECT * FROM usuarios WHERE login = ?", (login))
    login_dados = cursor.fetchall()
    banco.close()

    return login_dados


def inserir_rol_dados_qualitativos(lista, nome_table):
    banco = sql.connect('banco_cadastro.db')
    cursor = banco.cursor()

    nomes_tabelas = retornar_tables()
    if nome_table in nomes_tabelas:
        return 'Nome Table Error'
    else:
        try:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_table} (id INTEGER PRIMARY KEY AUTOINCREMENT, dado TEXT)")

            for dado in lista:
                dado = str(dado)
                if not any(char.isdigit() for char in dado):
                    cursor.execute(f"INSERT INTO {nome_table} (dado) VALUES (?)", (dado,))
                else:
                    cursor.execute(f"DROP TABLE IF EXISTS {nome_table}")
                    banco.commit()
                    return None

            banco.commit()
        except Exception as e:
            print(e)
            banco.rollback()
            return None
        finally:
            banco.close()
            return True


def inserir_rol_dados_quantitativos(lista, nome_table):
    banco = sql.connect('banco_cadastro.db')
    cursor = banco.cursor()

    nomes_tabelas = retornar_tables()
    if nome_table in nomes_tabelas:
        print("Entrou no error table")
        return 'Nome Table Error'
    else:
        try:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_table} (id INTEGER PRIMARY KEY AUTOINCREMENT, dado REAL)")
            for dado in lista:
                dado = float(dado)
                if isinstance(dado, float) or isinstance(dado, int):
                    cursor.execute(f"INSERT INTO {nome_table} (dado) VALUES (?)", (dado,))
                else:
                    cursor.execute(f"DROP TABLE IF EXISTS {nome_table}")
                    banco.commit()
                    return None
            banco.commit()
        except ValueError as e:
            cursor.execute(f"DROP TABLE IF EXISTS {nome_table}")
            banco.commit()
            banco.close()
            return "ValueError"
        except Exception as e:
            print(e)
            banco.rollback()
            banco.close()
            return None
        else:
            banco.close()
            return "Cadastrado"


def buscar_rol_dados(nome_table):
    lista_de_dados = []
    tabelas_banco = retornar_tables()
    for i, tabela_banco in enumerate(tabelas_banco):
        if nome_table == tabela_banco[:-2]:
            index = i
            nome_table = tabelas_banco[index]
            break
    try: 
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
    except Exception as e:
        print(e)
        banco.rollback()
    finally:
        banco.close()

    return lista_de_dados

def buscar_rol_dados_com_id(nome_table):
    lista_de_dados = []
    tabelas_banco = retornar_tables()
    for i, tabela_banco in enumerate(tabelas_banco):
        if nome_table == tabela_banco[:-2]:
            index = i
            nome_table = tabelas_banco[index]
            break
    try: 
        banco = sql.connect('banco_cadastro.db')
        cursor = banco.cursor()
        
        cursor.execute(f"SELECT * FROM {nome_table}")
        
        while True:
            dado = cursor.fetchone()
            if dado != None:
                lista_de_dados.append(dado)
            else:
                break
        banco.commit()
    except Exception as e:
        print(e)
        banco.rollback()
    finally:
        banco.close()

    return lista_de_dados


def atualizar_dado(lista, nome_table):
    try:
        banco = sql.connect("banco_cadastro.db")
        cursor = banco.cursor()

        cursor.execute(f"UPDATE {nome_table} SET dado = ? WHERE id = ?", (lista[1], lista[0]))
        banco.commit()
    except Exception as e:
        print(e)
        banco.rollback()
    finally:
        banco.close()


def deletar_registro(lista, nome_table):
    try:
        banco = sql.connect("banco_cadastro.db")
        cursor = banco.cursor()

        cursor.execute(f"DELETE FROM {nome_table} WHERE id = ?", (lista[0],))
        banco.commit()
    except Exception as e:
        print(e)
        banco.rollback()
    finally:
        banco.close()
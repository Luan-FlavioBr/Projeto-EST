def pegar_dados_qualitativos_txt(origem):
    lista = list()
    with open(origem, 'r', encoding="utf-8") as arquivo_origem:
        for dado in arquivo_origem:
            dado = dado.replace("\n", "").split(",")
            if not any(char.isdigit() for char in dado):
                lista.append(dado[0])
    return lista


def pegar_dados_quantitativos_txt(origem):
    lista = list()
    with open(origem, 'r', encoding="utf-8") as arquivo_origem:
        for dado in arquivo_origem:
            dado = dado.replace("\n", "").split(",")
            if isinstance(dado, float) or isinstance(dado, int):
                lista.append(dado[0])
    return lista
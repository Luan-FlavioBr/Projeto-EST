'''
Olá Luan do futuro, você estava na função carregar dados, você tem que colocar o SEGMENTBUTTON e o ScrollableFrame
Boa sorte! >:)
'''

import tkinter as tk
from tkinter import filedialog, PhotoImage, END, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
from CTkListbox import *
import os

from DBController import *
from cadastro import *
from conversaoTxt import *
from paretoExel import *
from tratamentos import *
from medidasDeTendencia import *
from funcaoBinomial import *


# Função da tela de cadastro
def cadastrar_clicado():
    tela_cadastrar_starter()


# Função da tela de login
elementos_login = list()
elementos_principal = list()
def adicionarElementos(*args, tipo):
    if tipo == 1:
        for element in args:
            elementos_login.append(element)
    else:
        for element in args:
            elementos_principal.append(element)


def mudarTemaLogin():
    if switchTheme.get() == "on":
        janela._set_appearance_mode("dark")
        frame_main_login._set_appearance_mode("dark") 
        frame_main_pricipal._set_appearance_mode("dark")
        frame_menu._set_appearance_mode("dark")
        for element in elementos_login:
            element._set_appearance_mode("dark") 
    else:
        janela._set_appearance_mode("light")
        frame_main_login._set_appearance_mode("light")
        frame_main_pricipal._set_appearance_mode("light")
        frame_menu._set_appearance_mode("light")
        button_cadastrar.configure(fg_color="#343638")
        for element in elementos_login:
            element._set_appearance_mode("light")


def mudarTemaPricipal():
    if switchTheme2.get() == "on":
        janela._set_appearance_mode("dark")
        frame_main_pricipal._set_appearance_mode("dark")
        frame_menu._set_appearance_mode("dark")
        for element in elementos_principal:
            element._set_appearance_mode("dark") 
    else:
        janela._set_appearance_mode("light")
        frame_main_pricipal._set_appearance_mode("light")
        frame_menu._set_appearance_mode("light")
        for element in elementos_principal:
            element._set_appearance_mode("light")


def login_clicado():
    login = entry_login.get()
    dados_login = verificar_cadastro(login)

    if dados_login == None or len(dados_login) == 0 :
        entry_login.configure(border_color="red")
    else:
        entry_login.configure(border_color="#565B5E")
        if entry_senha.get() != dados_login[0][1]:
            entry_senha.configure(border_color="red")
        else:
            entry_senha.configure(border_color="#565B5E")
        
        if entry_login.get() == dados_login[0][0] and entry_senha.get() == dados_login[0][1]:
            # Resetando frame
            global frame_main_login
            frame_main_pricipal.pack(fill='both', expand=True)
            frame_main_login.destroy()
            # Config janela principal!
            janela.title("Tela Principal")
            screen_width = janela.winfo_screenwidth()
            screen_height = janela.winfo_screenheight()

            w = 1200
            h = 600

            x = (screen_width/2) - (w/2)
            y = (screen_height/2) - (h/2)

            janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
            janela._set_appearance_mode('dark')
            janela.resizable(width=True, height=True)


# Funções da tela principal
def sair():
    janela.destroy()
    os._exit(0)


def digitarDados():
    frame_carregar.place(x=700, rely=-0.5, anchor="center")
    frame_digitar.place(x=700, rely=0.5, anchor="center")
    frame_analise_pareto.place(x=700, rely=-0.5, anchor="center")
    frame_editar_dados.place(x=700, rely=-0.5, anchor="center")
    frame_medidas_tendencia.place(x=700, rely=-0.5, anchor="center")
    frame_binomial.place(x=700, rely=-0.5, anchor="center")


def carregarDados():
    frame_digitar.place(x=700, rely=-0.5, anchor="center")
    frame_carregar.place(x=700, rely=0.5, anchor="center")
    frame_analise_pareto.place(x=700, rely=-0.5, anchor="center")
    frame_editar_dados.place(x=700, rely=-0.5, anchor="center")
    frame_medidas_tendencia.place(x=700, rely=-0.5, anchor="center")
    frame_binomial.place(x=700, rely=-0.5, anchor="center")


def analisePareto():
    frame_analise_pareto.place(x=700, rely=0.5, anchor="center")
    frame_digitar.place(x=700, rely=-0.5, anchor="center")
    frame_carregar.place(x=700, rely=-0.5, anchor="center")
    frame_editar_dados.place(x=700, rely=-0.5, anchor="center")
    frame_medidas_tendencia.place(x=700, rely=-0.5, anchor="center")
    frame_binomial.place(x=700, rely=-0.5, anchor="center")


def medidasTendencia():
    frame_medidas_tendencia.place(x=700, rely=0.5, anchor="center")
    frame_analise_pareto.place(x=700, rely=-0.5, anchor="center")
    frame_digitar.place(x=700, rely=-0.5, anchor="center")
    frame_carregar.place(x=700, rely=-0.5, anchor="center")
    frame_editar_dados.place(x=700, rely=-0.5, anchor="center")
    frame_binomial.place(x=700, rely=-0.5, anchor="center")


def binomial():
    frame_binomial.place(x=700, rely=0.5, anchor="center")
    frame_editar_dados.place(x=700, rely=-0.5, anchor="center")
    frame_analise_pareto.place(x=700, rely=-0.5, anchor="center")
    frame_digitar.place(x=700, rely=-0.5, anchor="center")
    frame_carregar.place(x=700, rely=-0.5, anchor="center")
    frame_medidas_tendencia.place(x=700, rely=-0.5, anchor="center")

def editarDados():
    frame_editar_dados.place(x=700, rely=0.5, anchor="center")
    frame_analise_pareto.place(x=700, rely=-0.5, anchor="center")
    frame_digitar.place(x=700, rely=-0.5, anchor="center")
    frame_carregar.place(x=700, rely=-0.5, anchor="center")
    frame_medidas_tendencia.place(x=700, rely=-0.5, anchor="center")
    frame_binomial.place(x=700, rely=-0.5, anchor="center")


# Funções frame carregar dados
def segmented_escolha(value):
    if value == "Banco de dados":
        texto = "Para utilizar o banco de dados como base para a Análise de Pareto ou cálculo de medidas, o mesmo deve ter sido utilizado pelo menos uma vez. Se for a primeira vez que você está usando o programa, faça o upload de um arquivo .txt ou Excel seguindo as normas. Caso não tenha nenhum desses arquivos, utilize a aba 'Digitar Dados' para inserção manual."
        label_frame_scroll_info.configure(text=texto, justify="left")
    elif value == "Arquivo .txt":
        texto = """Para utilizar um arquivo .txt como base de dados para a Análise de Pareto e cálculos de medidas, siga as seguintes normas para o correto funcionamento do programa:
    1 - Utilize "," (vírgula) para separar seus dados qualitativos ou quantitativos. 
    2 - Caso queira, marque a opção de guardar esses dados no banco de dados. 
    3 - Certifique-se de que o arquivo que será utilizado não esteja aberto enquanto o programa estiver em execução."""
        label_frame_scroll_info.configure(text=texto, justify="left")
    elif value == "Arquivo Exel":
        texto = """Para utilizar um arquivo exel como base de dados para a Análise de Pareto e cálculos de medidas, siga as seguintes normas para o correto funcionamento do programa:
    1 - Deixe todos seus dados apenas na coluna A. 
    2 - Caso queira, marque a opção de guardar esses dados no banco de dados. 
    3 - Certifique-se de que o arquivo que será utilizado não esteja aberto   enquanto o programa estiver em execução."""
        label_frame_scroll_info.configure(text=texto, justify="left")


def carregar_tabela_bd():
    for dados in tableDataBaseDados:
        table_baseDados.insert(parent='', index="end", values=(dados.split('\t')))


def limpar_tabela_bd():
    table_baseDados.delete(*table_baseDados.get_children())


def tela_error(mensagem):
    top_level_error = ctk.CTkToplevel(janela)
    top_level_error.title("Error")
    top_level_error.resizable(width=False, height=False)
    top_level_error.geometry('%dx%d+%d+%d' % (500, 250, x, y))

    label_error = ctk.CTkLabel(top_level_error, text=mensagem, font=("calibri bold", 16), wraplength=499, text_color="red")
    label_error.place(relx=0.5, rely=0.5, anchor="center")

    top_level_error.grab_set()


def tela_sucesso(mensagem):
    top_level_error = ctk.CTkToplevel(janela)
    top_level_error.title("Error")
    top_level_error.resizable(width=False, height=False)
    top_level_error.geometry('%dx%d+%d+%d' % (500, 250, x, y))

    label_error = ctk.CTkLabel(top_level_error, text=mensagem, font=("calibri bold", 16), wraplength=499, text_color="green")
    label_error.place(relx=0.5, rely=0.5, anchor="center")

    top_level_error.grab_set()


def escolherCaminhoArquivo():
    janela.focus_set()
    if radio_var.get() != 0:
        origem = filedialog.askopenfilename(initialdir="/Desktop",
                                            title="Abrir exel",
                                            filetypes = (("Arquivos Exel","*.xlsx"), ("Arquivos txt","*.txt")))

        resultado = salvar_no_bd(origem, f'{entry_nome_bd.get()}_{radio_var.get()}')
        
        if resultado == None:
            tela_error("Erro ao salvar conjunto de dados! Siga corretamente a formatação dos dados digitados!")
        elif resultado == "ValueError":
            if radio_var.get() == 1:
                tela_error("Erro ao salvar conjunto de dados! Seu aquivo contém dados qualitativos!")
            else:
                tela_error("Erro ao salvar conjunto de dados! Seu aquivo contém dados numéricos!")
        elif resultado == 'Nome Table Error':
            tela_error("O nome do conjunto de dados já existe!")
        elif resultado == "Max tables reached":
            tela_error("Número máximo de conjunto de dados alcançado, vá em Editar dados e exclua um conunto de sua preferencia!")
        else:
            tela_sucesso("Dados salvos!")
            atualizar_table_histograma()
            atualizar_table_pareto()
            atualizar_listbox_editar()


def salvar_no_bd(origem, nome_do_table):
    entry_nome_bd.delete(0, END)
    tipo_arquivo = origem.split('/')[-1].split(".")[-1]
    
    if tipo_arquivo == "txt":
        if radio_var.get() == 1:
            lista_de_dados = pegar_dados_quantitativos_txt(origem)
            return inserir_rol_dados_quantitativos(lista_de_dados, nome_do_table)
        elif radio_var.get() == 2:
            lista_de_dados = pegar_dados_qualitativos_txt(origem)
            return inserir_rol_dados_qualitativos(lista_de_dados, nome_do_table)
        elif radio_var.get() == 3:
            lista_de_dados = pegar_dados_qualitativos_txt(origem)
            return inserir_rol_dados_qualitativos(lista_de_dados, nome_do_table)
    elif tipo_arquivo == "xlsx":
        if radio_var.get() == 1:
            lista_de_dados= ler_dados_quantitativos_exel(origem)
            return inserir_rol_dados_quantitativos(lista_de_dados, nome_do_table)
        elif radio_var.get() == 2:
            lista_de_dados = pegar_dados_qualitativos_xlsx(origem)
            return inserir_rol_dados_qualitativos(lista_de_dados, nome_do_table)
        elif radio_var.get() == 3:
            lista_de_dados = pegar_dados_qualitativos_xlsx(origem)
            return inserir_rol_dados_qualitativos(lista_de_dados, nome_do_table)


# Funções frame digitar dados
# Não deixa mexer no tamanho da coluna da table
def prevent_resize(event):
    if table.identify_region(event.x, event.y) == "separator":
        return "break"


def adicionar_item():
    dados = entry_dados.get()
    if dados != '' and dados.strip() != "":
        formatado = dados.split(',')
        for i,item in enumerate(formatado):
            formatado[i] = item.strip() 

        for dado in formatado:
            if dado != "":
                tableData.append(dado)
                table.insert(parent='', index='end', values=(dado.split('\t')))
        entry_dados.delete(0, END)
        frame_digitar.focus_set()


def carregar_tabela():
    for dados in tableData:
        table.insert(parent='', index="end", values=(dados.split('\t')))


# Apaga todos os dados da tabela
def limpar_tabela():
    table.delete(*table.get_children())


def pegar_item(event):
    def atualizar_item(valor_antigo, novo_valor):
        indice = tableData.index(valor_antigo)
        tableData[indice] = novo_valor
        limpar_tabela()
        carregar_tabela()
        top_level.destroy()


    def deletar_item(valor):
        tableData.pop(tableData.index(valor[0]))
        limpar_tabela()
        carregar_tabela()
        top_level.destroy()


    selecionado = table.selection()
    
    if selecionado:
        item_selecionado = selecionado[0]
        valor_linha = table.item(item_selecionado, 'values')
        
        top_level = ctk.CTkToplevel(janela)

        top_level.title("Alteração de dado")
        top_level.geometry('%dx%d+%d+%d' % (500, 250, x, y))

        label = ctk.CTkLabel(top_level, text="Editar ou deletar dado", font=("arial norma", 15))
        label.place(rely=0.05, relx=0.5, anchor='center')

        entry_alteracao = ctk.CTkEntry(top_level, width=350, height=35)
        entry_alteracao.place(rely=0.45, relx=0.5, anchor="center")
        entry_alteracao.insert(0, valor_linha[0])

        button_deletar = ctk.CTkButton(top_level, text="Deletar", command=lambda: deletar_item(valor_linha))
        button_deletar.place(rely=0.65, relx=0.35, anchor="center")

        button_update = ctk.CTkButton(top_level, text="Atualizar", command=lambda: atualizar_item(valor_linha[0], entry_alteracao.get()))
        button_update.place(rely=0.65, relx=0.65, anchor="center")


def inserirDados_noBD():
    global tableData
    if radio_var_digitar.get() != 0:
        nome_bd = f'{entry_nome_bd_digitar.get()}_{radio_var_digitar.get()}'
        if radio_var_digitar.get() == 2 or radio_var_digitar.get() == 3: 
            resultado = inserir_rol_dados_qualitativos(tableData, nome_bd)
        else:
            resultado = inserir_rol_dados_quantitativos(tableData, nome_bd)
        entry_nome_bd_digitar.delete(0, END)
        limpar_tabela()
        tableData = list()
        if resultado == None:
            tela_error("Erro ao salvar conjunto de dados! Siga corretamente a formatação dos dados digitados!")
        elif resultado == "ValueError":
            if radio_var_digitar.get() == 1:
                tela_error("Erro ao salvar conjunto de dados! Você digitou dados qualitativos!")
            else:
                tela_error("Erro ao salvar conjunto de dados! Você digitou dados numéricos!")
        elif resultado == 'Nome Table Error':
            tela_error("O nome do conjunto de dados já existe!")
        else:
            atualizar_listbox_editar()
            tela_sucesso("Dados salvos!")
            if radio_var_digitar.get() == 1:
                atualizar_table_histograma()
            else:
                atualizar_table_pareto()
        


def verificar_tipo_table(nome_table):
    tabelas_banco = retornar_tables()
    for i, tabela_banco in enumerate(tabelas_banco):
        if nome_table == tabela_banco[:-2]:
            index = i
            nome_table = tabelas_banco[index]
            return int(nome_table[-1:])


# Frame Análise Pareto
def gerarAnalisePareto(gerarAnalise):
    from PIL import Image


    def sair_top():
        top_level.destroy()


    selecionado = table_baseDados.selection()
    if selecionado:
        item_selecionado = selecionado[0]
        valor_linha = table_baseDados.item(item_selecionado, 'values')
        top_level = ctk.CTkToplevel(janela)
 
        top_level.title("Análise de Pareto")
        top_level.geometry('%dx%d+%d+%d' % (800, 400, x, y))
        top_level.resizable(width=False, height=False)

        origem = filedialog.askdirectory(initialdir="/Desktop",
                                            title="Abrir exel")
        
        lista_quali = buscar_rol_dados(valor_linha[0])
        tipo_table = verificar_tipo_table(valor_linha[0])

        if tipo_table == 3:
            lista_quali_temp = list(set(lista_quali))
            custo_de_ocorrencia = list()
            for i in lista_quali_temp:
                while True:
                    custo = ctk.CTkInputDialog(text=f"Insira o custo da ocorrência: {i}", title="Insira o custo")
                    custo.geometry('%dx%d+%d+%d' % (350, 200, x, y))
                    custo_produto = lerfloat(custo.get_input())
                    if custo_produto != None:
                        custo_de_ocorrencia.append(custo_produto)
                        break
            localDoArquivo = operacoesExel(origem, origem, lista_quali, 2, custo_de_ocorrencia)
        else:
            localDoArquivo = operacoesExel(origem, origem, lista_quali, 1)

        scroll_frame_pareto = ctk.CTkScrollableFrame(top_level)
        scroll_frame_pareto.pack(fill="both", expand=True)

        label_titulo = ctk.CTkLabel(scroll_frame_pareto, text="Tabela de Análise de Pareto", width=200, height=35, font=("calibri bold", 24))
        label_titulo.pack()

        # Fazendo a tabela de análise de pareto
        tableColumns = list()

        if tipo_table != 3:
            tableColumns = ['Tipo de falha','Nº de Ocorrências','Fr(%)', 'Fr Acum(%)']
        else:
            tableColumns = ['Tipo de falha','Nº de Ocorrências','Impacto de custo/ocorr.','Total','Fr(%)', 'Fr Acum(%)']

        tablePareto = ttk.Treeview(master=scroll_frame_pareto, columns=tableColumns, show="headings")
        for column in tableColumns:
            tablePareto.heading(column=column, text=column)
            tablePareto.column(column=column, width=150)

        tablePareto.column("Nº de Ocorrências", anchor='e')
        tablePareto.column("Fr(%)", anchor='e')
        tablePareto.column("Fr Acum(%)", anchor='e')

        if tipo_table == 3:
            tablePareto.column("Impacto de custo/ocorr.", anchor='e')
            tablePareto.column("Total", anchor='e')

        stylePareto = ttk.Style()
        stylePareto.theme_use('default')
        stylePareto.configure("Treeview.Heading", background="#1F6AA5", foreground="white", font=("arial bold", 15), borderwidth=0, relief = 'flat')
        stylePareto.map("Treeview.Heading", background=[("pressed", "!focus", "#1F6AA5"), ("active", "#1F6AA5"), ("disabled", "white")])

        stylePareto.configure("Treeview", background="#343638", fieldbackground="#242424", foreground="white",
                        corner_radius=15, borderwidth=1)
        
        if tipo_table != 3:
            tableDataPareto = lerarquivo(localDoArquivo, 1)
        else:
            tableDataPareto = lerarquivo(localDoArquivo, 2)
        
        for rowData in tableDataPareto:
            tablePareto.insert(parent='', index='end', values=rowData)
        
        tablePareto.pack()
        
        label_titulo_grafico = ctk.CTkLabel(scroll_frame_pareto, text="Gráfico de Pareto", font=("calibri bold", 24))
        label_titulo_grafico.pack(pady=50) 

        if tipo_table != 3:
            localDaImagem = aplicacaoGraficoPareto(localDoArquivo, gerarAnalise, 1)
        else:
            localDaImagem = aplicacaoGraficoPareto(localDoArquivo, gerarAnalise, 2)

        my_image = ctk.CTkImage(light_image=Image.open(localDaImagem),
                                  dark_image=Image.open(localDaImagem),
                                  size=(600, 300))

        image_label = ctk.CTkLabel(scroll_frame_pareto, image=my_image, text="").pack()
        
        top_level.grab_set()
        top_level.protocol("WM_DELETE_WINDOW", sair_top)


def gerarHistograma(gerarExel):
    from PIL import Image


    def sair_top():
        top_level.destroy()


    selecionado = listbox_de_tabelas_medidas.get()
    if selecionado:

        origem = filedialog.askdirectory(initialdir="/Desktop",
                                            title="Abrir exel")

        rol_de_dados = buscar_rol_dados(f'{selecionado}_1')
        localArquivo = realizarMedidas(rol_de_dados, origem)

        top_level = ctk.CTkToplevel(janela)
    
        top_level.title("Histograma")
        top_level.geometry('%dx%d+%d+%d' % (800, 400, x, y))
        top_level.resizable(width=False, height=False)

        scroll_frame_histograma = ctk.CTkScrollableFrame(top_level)
        scroll_frame_histograma.pack(fill="both", expand=True)

        # Tabela medidas centrais
        label_medidas_centrais = ctk.CTkLabel(scroll_frame_histograma, text="Tabela de medidas centrais", font=("calibri bold", 24))
        label_medidas_centrais.pack()

        tableColumnsMedidasCentrais = ['Titulos','Valores']
        tableDataMedidasCentrais = retornar_dados_medidas_t_central(localArquivo)
        tableMedidasCentrais = ttk.Treeview(master=scroll_frame_histograma, columns=tableColumnsMedidasCentrais, show="headings",
                                            height=len(tableDataMedidasCentrais))
        for column in tableColumnsMedidasCentrais:
            tableMedidasCentrais.heading(column=column, text=column)
            tableMedidasCentrais.column(column=column, width=150)
        # Inserindo na lista de medidas centrais
        for rowData in tableDataMedidasCentrais:
            tableMedidasCentrais.insert(parent='', index='end', values=rowData)
        
        tableMedidasCentrais.column(tableColumnsMedidasCentrais[1], anchor='e')
        tableMedidasCentrais.pack()

        # Tabela intervalo de classe
        label_intervalo_classe = ctk.CTkLabel(scroll_frame_histograma, text="Tabela de intervalo de classe", font=("calibri bold", 24))
        label_intervalo_classe.pack(pady=20)

        tableColumnsIntervaloClasse = ['Titulos','Valores']
        tableDataIntervaloClasse = retornar_dados_intervalo_classe(localArquivo)
        tableIntervaloClasse = ttk.Treeview(master=scroll_frame_histograma, columns=tableColumnsIntervaloClasse, show="headings", height=5)
        for column in tableColumnsIntervaloClasse:
            tableIntervaloClasse.heading(column=column, text=column)
            tableIntervaloClasse.column(column=column, width=250)
        # Inserindo na lista de intervalos de classe
        for rowData in tableDataIntervaloClasse:
            tableIntervaloClasse.insert(parent='', index='end', values=rowData)

        tableIntervaloClasse.column(tableColumnsIntervaloClasse[1], anchor='e')
        tableIntervaloClasse.pack()

        # Tabela de frequência
        label_frequencia = ctk.CTkLabel(scroll_frame_histograma, text="Tabela de frenquencia", font=("calibri bold", 24))
        label_frequencia.pack(pady=20)

        tableColumnsFrequencia = ['Frequências','Ponto Médio', 'Fi', 'Fr', 'Fr(%)', 'Fr acum(%)']
        tableDataFrequencia = dado_para_tabela(localArquivo)
        tableFrequencia = ttk.Treeview(master=scroll_frame_histograma, columns=tableColumnsFrequencia, show="headings",
                                       height=len(tableDataFrequencia)-1)
        for column in tableColumnsFrequencia:
            tableFrequencia.heading(column=column, text=column)
            tableFrequencia.column(column=column, width=150)
        for rowData in tableDataFrequencia:
            if rowData != tableDataFrequencia[0]:
                tableFrequencia.insert(parent='', index='end', values=rowData)

        tableFrequencia.column(tableColumnsFrequencia[2], anchor='e')
        tableFrequencia.column(tableColumnsFrequencia[3], anchor='e')
        tableFrequencia.column(tableColumnsFrequencia[4], anchor='e')
        tableFrequencia.column(tableColumnsFrequencia[5], anchor='e')
        tableFrequencia.pack()

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="#1F6AA5", foreground="white", font=("arial", 14), borderwidth=0, relief = 'flat')
        style.configure("Treeview.Heading", background="#1F6AA5", foreground="white", font=("Calibri bold", 17), borderwidth=0, relief = 'flat')
        style.map("Treeview.Heading", background=[("pressed", "!focus", "#1F6AA5"), ("active", "#1F6AA5"), ("disabled", "white")])

        style.configure("Treeview", background="#343638", fieldbackground="#242424", foreground="white",
                        corner_radius=15, borderwidth=1)

        label_histograma = ctk.CTkLabel(scroll_frame_histograma, text="Gráfico Histograma", font=("calibri bold", 24))
        label_histograma.pack(pady=20)

        localImagem = realizar_grafico(origem, gerarExel)
        my_image = ctk.CTkImage(light_image=Image.open(localImagem),
                                  dark_image=Image.open(localImagem),
                                  size=(600, 300))

        image_label = ctk.CTkLabel(scroll_frame_histograma, image=my_image, text="").pack()

        top_level.grab_set()
        top_level.protocol("WM_DELETE_WINDOW", sair_top)


def validarBinomio(n, p):
    n = lerint(n)
    p = lerfloat(p)
    if isinstance(n, int) and (isinstance(p, float) or isinstance(p, int)):
        button_gerar_graficobinomial.place(relx=0.50, rely=0.90, anchor="center")
        global tableDataBinomial
        global caminhoImagem
        entry_p.configure(border_color="#565B5E")
        entry_n.configure(border_color="#565B5E")
        listaValores, caminhoImagemLocal = calcularBinomio(n, p)
        tableDataBinomial = listaValores
        caminhoImagem = caminhoImagemLocal
        tableBinomial.delete(*tableBinomial.get_children())
        for dados in tableDataBinomial:
            tableBinomial.insert(parent='', index="end", values=(dados))
    else:
        if n == None:
            entry_n.configure(border_color="red")
        else:
            entry_n.configure(border_color="#565B5E")
        
        if p == None:
            entry_p.configure(border_color="red")
        else:
            entry_p.configure(border_color="#565B5E")


def acumular(event):
    total = 0
    itensSelecionados = tableBinomial.selection()
    for i in itensSelecionados:
        total = float(tableBinomial.item(i)["values"][1]) + total
    label_totalAcum.configure(text=f"Total acumulado: {total:.2%}") 


def abrirGraficoBinomial():
    from PIL import Image
    top_level_grafico_binomial = ctk.CTkToplevel(janela)
 
    top_level_grafico_binomial.title("Gráfico Binomial")
    top_level_grafico_binomial.geometry('%dx%d+%d+%d' % (1000, 600, x, y))
    top_level_grafico_binomial.resizable(width=False, height=False)

    my_image = ctk.CTkImage(light_image=Image.open(caminhoImagem),
                                  dark_image=Image.open(caminhoImagem),
                                  size=(1000, 600))

    image_label = ctk.CTkLabel(top_level_grafico_binomial, image=my_image, text="").pack()
    top_level_grafico_binomial.grab_set()


def abrir_top_crud(selecionado):
    def limpar_tabela_dados():
        table_Dados.delete(*table_Dados.get_children())


    def carregar_tabela_dados():
        global tableDataDadosReturns
        tableDataDadosReturns = buscar_rol_dados_com_id(selecionado)

        for dados in tableDataDadosReturns:
            table_Dados.insert(parent='', index="end", values=(dados))


    def atualizar_item(valor):
        valor[1] = entry_editar_dados.get()
        valor[0] = int(valor[0])
        atualizar_dado(valor, selecionado)

        limpar_tabela_dados()
        carregar_tabela_dados()


    def deletar_item(valor):
        deletar_registro(valor, selecionado)
        limpar_tabela_dados()
        carregar_tabela_dados()

    def item_pego(event):
        entry_editar_dados.delete(0, END)
        linha_selecionada = table_Dados.selection()

        if linha_selecionada:
            item_selecionado = linha_selecionada[0]
            valor_linha = table_Dados.item(item_selecionado, 'values')

            entry_editar_dados.configure(state="normal")
            entry_editar_dados.insert(0, valor_linha[1])
            
            button_editar_dado.configure(command=lambda:atualizar_item(list(valor_linha)))

            button_deletar_dado.configure(command=lambda:deletar_item(list(valor_linha)))


    def deletarTable(nome_table):
        drop_table(nome_table)
        top_level_editar_dados.destroy()
        frame_editar_dados.grab_set()
        atualizar_listbox_editar()
        atualizar_table_histograma()
        atualizar_table_pareto()


    dados_retornados = buscar_rol_dados_com_id(selecionado)

    top_level_editar_dados = ctk.CTkToplevel(janela)
 
    top_level_editar_dados.title("Análise de Pareto")
    top_level_editar_dados.geometry('%dx%d+%d+%d' % (900, 500, x, y))
    top_level_editar_dados.resizable(width=False, height=False)

    tableColumnsDadosReturns = ['ID', "Dados"]
    tableDataDadosReturns = dados_retornados

    table_Dados = ttk.Treeview(master=top_level_editar_dados, columns=tableColumnsDadosReturns, show="headings")
    for column in tableColumnsDadosReturns:
        table_Dados.heading(column=column, text=column)
        table_Dados.column(column=column, width=250)

    table_Dados.column("ID", anchor='e', width=65)
    table_Dados.column("Dados", anchor='e', width=335)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#1F6AA5", foreground="white", font=("arial", 14), borderwidth=0, relief = 'flat')
    style.configure("Treeview.Heading", background="#1F6AA5", foreground="white", font=("Calibri bold", 17), borderwidth=0, relief = 'flat')
    style.map("Treeview.Heading", background=[("pressed", "!focus", "#1F6AA5"), ("active", "#1F6AA5"), ("disabled", "white")])

    style.configure("Treeview", background="#343638", fieldbackground="#242424", foreground="white",
                    corner_radius=15, borderwidth=1)


    table_Dados.place(rely=0.35, relx=0.5, anchor="center")

    table_Dados.bind('<Motion>', prevent_resize)
    table_Dados.bind('<<TreeviewSelect>>', item_pego)

    for dados in tableDataDadosReturns:
        table_Dados.insert(parent='', index="end", values=(dados))

    entry_editar_dados = ctk.CTkEntry(top_level_editar_dados, width=350, height=35, placeholder_text="Dado", state="disabled")
    entry_editar_dados.place(rely=0.65, relx=0.5, anchor="center")

    button_editar_dado = ctk.CTkButton(top_level_editar_dados, width=150, height=35, text="Alterar")
    button_editar_dado.place(rely=0.75, relx=0.40, anchor="center")

    button_deletar_dado = ctk.CTkButton(top_level_editar_dados, width=150, height=35, text="Deletar")
    button_deletar_dado.place(rely=0.75, relx=0.60, anchor="center")

    button_deletar_table = ctk.CTkButton(top_level_editar_dados, width=150, height=35, 
                                         text="Deletar conjunto de dados", command=lambda: deletarTable(selecionado))
    button_deletar_table.place(rely=0.85, relx=0.50, anchor="center")

    top_level_editar_dados.grab_set()


def atualizar_listbox_editar():
    global lista_de_tabelas_bd
    lista_de_tabelas_bd = retornar_tables()
    if len(lista_de_tabelas_bd) > 1:
        listbox_de_tabelas.delete(0, END)
    for i, nome_tabela in enumerate(lista_de_tabelas_bd):
        listbox_de_tabelas.insert(i, nome_tabela)


def atualizar_table_pareto():
    global tableDataBaseDados
    tableDataBaseDados = retornar_tables_pareto()
    limpar_tabela_bd()
    carregar_tabela_bd()


def atualizar_table_histograma():
    global lista_de_tabelas_bd_medidas
    lista_de_tabelas_bd_medidas = retornar_tables_histograma()
    for i, nome_tabela in enumerate(lista_de_tabelas_bd_medidas):
        listbox_de_tabelas_medidas.insert(i, nome_tabela)

# Início Programa
janela = ctk.CTk()

# Tela Login!
janela.title("Tela Login")
janela.resizable(width=False, height=False)
janela.protocol("WM_DELETE_WINDOW", sair)
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

x = (screen_width/2) - (400/2)
y = (screen_height/2) - (300/2)

janela.geometry('%dx%d+%d+%d' % (300, 400, x, y))

font_negrito = ('arial bold', 18)

# Definindo Frame principal do login
frame_main_login = ctk.CTkFrame(janela)
frame_main_login.pack(fill="both", expand=True)
# Fim definição

label_login = ctk.CTkLabel(frame_main_login, text="LOGIN", font= font_negrito)
label_login.place(relx=0.25, y=100, anchor="center")
entry_login = ctk.CTkEntry(frame_main_login, width=210, placeholder_text="Digite seu login")
entry_login.place(relx=0.5, y=130, anchor="center")

label_senha = ctk.CTkLabel(frame_main_login, text="SENHA", font= font_negrito)
label_senha.place(relx=0.25, y=168, anchor="center")
entry_senha = ctk.CTkEntry(frame_main_login, width=210, placeholder_text="Digite sua senha", show='*')
entry_senha.place(relx=0.5, y=198, anchor="center")

button_login = ctk.CTkButton(frame_main_login, width=200, text="Logar", command=login_clicado)
button_login.place(relx=0.5, y=238, anchor="center")

button_cadastrar = ctk.CTkButton(frame_main_login, width=200, text="Não tem cadastro? Clique aqui!", 
                                fg_color='transparent', hover_color='#444444', command=cadastrar_clicado)
button_cadastrar.place(relx=0.5, y=268, anchor="center")

switch_var_principal = ctk.StringVar(value='on')

switchTheme = ctk.CTkSwitch(frame_main_login, text="Tema", command=mudarTemaLogin, 
                            variable=switch_var_principal, onvalue='on', offvalue="off")
switchTheme.place(relx=0.20, rely=0.90, anchor="center")

# Fim Tela Login
# ----------------------------------------------------------------------------------------------------------------------------------------
# Tela Pricipal
frame_main_pricipal = ctk.CTkFrame(janela)

# Posicionando Frames
frame_carregar = ctk.CTkFrame(frame_main_pricipal, width=1040, height=600, fg_color="#242424")
frame_carregar.place(x=700, rely=-0.5, anchor="center")

frame_digitar = ctk.CTkFrame(frame_main_pricipal, width=1040, height=600, fg_color="#242424")
frame_digitar.place(x=700, rely=-0.5, anchor="center")

frame_analise_pareto = ctk.CTkFrame(frame_main_pricipal, width=1040, height=600, fg_color="#242424")
frame_analise_pareto.place(x=700, rely=-0.5, anchor="center")

frame_medidas_tendencia = ctk.CTkFrame(frame_main_pricipal, width=1040, height=600, fg_color="#242424")
frame_medidas_tendencia.place(x=700, rely=-0.5, anchor="center")

frame_binomial = ctk.CTkFrame(frame_main_pricipal, width=1040, height=600, fg_color="#242424")
frame_binomial.place(x=700, rely=-0.5, anchor="center")

frame_editar_dados = ctk.CTkFrame(frame_main_pricipal, width=1040, height=600, fg_color="#242424")
frame_editar_dados.place(x=700, rely=-0.5, anchor="center")

# Fim posicionamento

# Fonts
font_negrito = ('arial bold', 18)
font_normal = ('arial normal', 15)
font_normal18 = ('arial normal', 18)
#Fim Fonts

# Inicio tela principal
frame_menu = ctk.CTkFrame(frame_main_pricipal, width=180, height=600)
frame_menu.place(x=0, y=0)


button_carregar_dados = ctk.CTkButton(master=frame_menu, width=170, height=35, corner_radius=15, 
                                text="Carregar documentos", font=font_normal, command=carregarDados)
button_carregar_dados.place(y=30, x=90, anchor="center")


button_digitar_dados = ctk.CTkButton(master=frame_menu, width=170, height=35, corner_radius=15, 
                                text="Digitar Dados", font=font_normal, command=digitarDados)
button_digitar_dados.place(y=75, x=90, anchor="center")


button_pareto = ctk.CTkButton(master=frame_menu, width=170, height=35, corner_radius=15, 
                                text="Análise de Pareto", font=font_normal, command=analisePareto)
button_pareto.place(y=120, x=90, anchor="center")


button_medidas = ctk.CTkButton(master=frame_menu, width=170, height=35, corner_radius=15, 
                                text="Medidas e tabelas", font=font_normal, command=medidasTendencia)
button_medidas.place(y=165, x=90, anchor="center")

button_binomial = ctk.CTkButton(master=frame_menu, width=170, height=35, corner_radius=15, 
                                text="Cálculo Binomial", font=font_normal, command=binomial)
button_binomial.place(y=210, x=90, anchor="center")

button_editar = ctk.CTkButton(master=frame_menu, width=170, height=35, corner_radius=15, 
                                text="Editar dados", font=font_normal, command=editarDados)
button_editar.place(y=255, x=90, anchor="center")


switchTheme2 = ctk.CTkSwitch(master=frame_menu, text="Tema", command=mudarTemaPricipal, variable=switch_var_principal, 
                            onvalue='on', offvalue="off", font=font_normal)
switchTheme2.place(x=90, rely=0.85, anchor="center")


button_sair = ctk.CTkButton(master=frame_menu, width=170, height=35, corner_radius=15, 
                                text="Sair", font=font_normal, command=sair)
button_sair.place(rely=0.95, x=90, anchor="center")

# Fim Tela Pricipal
# ----------------------------------------------------------------------------------------------------------------------------------------
# Inicio Frame Carregar Dados

label_carregar_dados = ctk.CTkLabel(frame_carregar, text='Carregar Dados', fg_color="transparent",font=('arial normal', 24))
label_carregar_dados.place(relx=0.5, rely=0.05, anchor="center")

segmented_valor = ctk.StringVar(value="Selecione")
segmented_button = ctk.CTkSegmentedButton(frame_carregar, values=["Banco de dados", "Arquivo .txt", "Arquivo Exel"],
                                          command=segmented_escolha, variable=segmented_valor, width=200,height=45, 
                                          border_width=5, corner_radius=15)
segmented_button.place(relx= 0.5, rely=0.15, anchor="center")


frame_scroll_infos = ctk.CTkScrollableFrame(frame_carregar, width=500, height=250)
frame_scroll_infos.place(relx= 0.5, rely=0.41, anchor="center")

label_frame_scroll_info = ctk.CTkLabel(frame_scroll_infos, text="Selecione a opção", width=300, justify="left", wraplength=499,
                                       font=font_normal)
label_frame_scroll_info.pack()

radio_var = ctk.IntVar(value=0)
radio_button_1 = ctk.CTkRadioButton(frame_carregar, text="Quantitativo",
                                            variable= radio_var, value=1)
radio_button_1.place(relx=0.35, rely=0.67, anchor="center")


radio_button_2 = ctk.CTkRadioButton(frame_carregar, text="Qualitativo",
                                            variable= radio_var, value=2)
radio_button_2.place(relx=0.5, rely=0.67, anchor="center")


radio_button_3 = ctk.CTkRadioButton(frame_carregar, text="Ambos",
                                            variable= radio_var, value=3)
radio_button_3.place(relx=0.65, rely=0.67, anchor="center")


entry_nome_bd = ctk.CTkEntry(frame_carregar, placeholder_text="Digite o nome do Banco de Dados", width=275, height=35)
entry_nome_bd.place(relx=0.5, rely=0.75, anchor="center")


button_selecionar_arquivo = ctk.CTkButton(frame_carregar, text="Selecionar Arquivo", width=235, 
                                          height=45, corner_radius=15, command=escolherCaminhoArquivo)
button_selecionar_arquivo.place(relx=0.5, rely=0.85, anchor="center")

# Fim frame carregar Dados
# ----------------------------------------------------------------------------------------------------------------------------------------
# Incio frame digitar dados

label_carregar_dados = ctk.CTkLabel(frame_digitar, text='Digitar Dados', font=('arial normal', 24))
label_carregar_dados.place(relx=0.5, rely=0.05, anchor="center")

entry_dados = ctk.CTkEntry(frame_digitar, placeholder_text="Digite seus dados, quantitativo ou qualitativo",
                           width=275, height=35)
entry_dados.place(relx=0.5, rely=0.15, anchor="center")

button_inserir_dado = ctk.CTkButton(frame_digitar, width=275, height=35, 
                                    text="Inserir dado", command=adicionar_item)
button_inserir_dado.place(relx=0.5, rely=0.21, anchor="center")

tableColumns = ['Dados']
tableData = []

table = ttk.Treeview(master=frame_digitar, columns=tableColumns, show="headings")
for column in tableColumns:
    table.heading(column=column, text=column)
    table.column(column=column, width=350)


table.bind('<<TreeviewSelect>>', pegar_item)
table.bind('<Motion>', prevent_resize)

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview.Heading", background="#1F6AA5", foreground="white", font=("arial bold", 15), borderwidth=0, relief = 'flat')
style.map("Treeview.Heading", background=[("pressed", "!focus", "#1F6AA5"), ("active", "#1F6AA5"), ("disabled", "white")])

style.configure("Treeview", background="#343638", fieldbackground="#242424", foreground="white",
                corner_radius=15, borderwidth=1)

table.place(rely=0.5, relx=0.5, anchor="center")

radio_var_digitar = ctk.IntVar(value=0)
radio_button_1_digitar = ctk.CTkRadioButton(frame_digitar, text="Quantitativo",
                                            variable= radio_var_digitar, value=1)
radio_button_1_digitar.place(relx=0.35, rely=0.75, anchor="center")


radio_button_3_digitar = ctk.CTkRadioButton(frame_digitar, text="Qualitativo",
                                            variable= radio_var_digitar, value=2)
radio_button_3_digitar.place(relx=0.5, rely=0.75, anchor="center")


radio_button_3_digitar = ctk.CTkRadioButton(frame_digitar, text="Ambos",
                                            variable= radio_var_digitar, value=3)
radio_button_3_digitar.place(relx=0.65, rely=0.75, anchor="center")

entry_nome_bd_digitar = ctk.CTkEntry(frame_digitar, width=275, height=45, corner_radius=15,
                                     placeholder_text="Digite o nome do conjunto de dados")
entry_nome_bd_digitar.place(relx=0.5, rely=0.83, anchor="center")

button_inserir_rol_dados = ctk.CTkButton(frame_digitar, width=235, height=45, corner_radius=15,
                                         text="Salvar no banco de dados", command=inserirDados_noBD)
button_inserir_rol_dados.place(relx=0.5, rely=0.93, anchor="center")

# Fim frame digitar dados
# ----------------------------------------------------------------------------------------------------------------------------------------
# Inicio frame análise pareto

label_analise_pareto = ctk.CTkLabel(frame_analise_pareto, text='Análise Pareto', font=('arial normal', 24))
label_analise_pareto.place(relx=0.5, rely=0.05, anchor="center")

tableColumnsBaseDados = ['Base de Dados']
tableDataBaseDados = retornar_tables_pareto()

table_baseDados = ttk.Treeview(master=frame_analise_pareto, columns=tableColumnsBaseDados, show="headings")
for column in tableColumnsBaseDados:
    table_baseDados.heading(column=column, text=column)
    table_baseDados.column(column=column, width=550)

table_baseDados.bind('<Motion>', prevent_resize)

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="#1F6AA5", foreground="white", font=("arial", 14), borderwidth=0, relief = 'flat')
style.configure("Treeview.Heading", background="#1F6AA5", foreground="white", font=("Calibri bold", 17), borderwidth=0, relief = 'flat')
style.map("Treeview.Heading", background=[("pressed", "!focus", "#1F6AA5"), ("active", "#1F6AA5"), ("disabled", "white")])

style.configure("Treeview", background="#343638", fieldbackground="#242424", foreground="white",
                corner_radius=15, borderwidth=1)


table_baseDados.place(rely=0.35, relx=0.5, anchor="center")

for dados in tableDataBaseDados:
    table_baseDados.insert(parent='', index="end", values=(dados.split('\t')))

button_gerar_analisepareto = ctk.CTkButton(frame_analise_pareto, text="Gerar análise de pareto", 
                                           width=235, height=45, corner_radius=15, font=("arial", 15), 
                                           command=lambda:gerarAnalisePareto(checkbox_gerar_exel.get()))
button_gerar_analisepareto.place(relx=0.5, rely=0.75, anchor="center")

check_var = ctk.StringVar(value=True)
checkbox_gerar_exel = ctk.CTkCheckBox(frame_analise_pareto, text="Gerar arquivo exel",
                           variable=check_var, onvalue=True, offvalue=False)
checkbox_gerar_exel.place(relx=0.5, rely=0.85, anchor="center")

# Fim frame análise pareto
# ----------------------------------------------------------------------------------------------------------------------------------------
# Incio frame medidas e tabelas
label_medidas_tendencia = ctk.CTkLabel(frame_medidas_tendencia, text='Medidas de tendência central', font=('arial normal', 24))
label_medidas_tendencia.place(relx=0.5, rely=0.05, anchor="center")

label_titulo_listbox = ctk.CTkLabel(frame_medidas_tendencia, text='Escolha o conjunto de dados', font=('arial normal', 18))
label_titulo_listbox.place(relx=0.5, rely=0.15, anchor="center")

listbox_de_tabelas_medidas = CTkListbox(frame_medidas_tendencia, width=550, height=250)
listbox_de_tabelas_medidas.place(relx=0.5, rely=0.5, anchor="center")

lista_de_tabelas_bd_medidas = retornar_tables_histograma()
for i, nome_tabela in enumerate(lista_de_tabelas_bd_medidas):
    listbox_de_tabelas_medidas.insert(i, nome_tabela)

button_gerar_histograma = ctk.CTkButton(frame_medidas_tendencia, text="Gerar histograma", 
                                        width=235, height=45, corner_radius=15, font=("arial", 15),
                                        command=lambda:gerarHistograma(checkbox_gerar_exel_histograma.get()))
button_gerar_histograma.place(relx=0.5, rely=0.82, anchor="center")

check_var_histograma = ctk.StringVar(value=True)
checkbox_gerar_exel_histograma = ctk.CTkCheckBox(frame_medidas_tendencia, text="Gerar arquivo exel",
                                                 variable=check_var_histograma, onvalue=True, offvalue=False)
checkbox_gerar_exel_histograma.place(relx=0.5, rely=0.92, anchor="center")

# # Fim frame medidas e tabelas
# ----------------------------------------------------------------------------------------------------------------------------------------
# Inicío frame binomial
label_binomial = ctk.CTkLabel(frame_binomial, text='Cálculo Binomial', font=('arial normal', 24))
label_binomial.place(relx=0.5, rely=0.05, anchor="center")

label_n = ctk.CTkLabel(frame_binomial, text="n", font=('arial normal', 24))
label_n.place(relx=0.18, rely=0.20, anchor="center")
entry_n = ctk.CTkEntry(frame_binomial, width=275, height=45, corner_radius=15,
                        placeholder_text="Digite o número de ensaios")
entry_n.place(relx=0.33, rely=0.20, anchor="center")

label_p = ctk.CTkLabel(frame_binomial, text="p", font=('arial normal', 24))
label_p.place(relx=0.55, rely=0.20, anchor="center")
entry_p = ctk.CTkEntry(frame_binomial, width=275, height=45, corner_radius=15,
                        placeholder_text="Digite o número de tentativas")
entry_p.place(relx=0.70, rely=0.20, anchor="center")

button_gerar_binomial = ctk.CTkButton(frame_binomial, text="Gerar Cálculo Binomial", 
                                        width=235, height=45, corner_radius=15, font=("arial", 15), 
                                        command=lambda:validarBinomio(entry_n.get(), entry_p.get()))
button_gerar_binomial.place(relx=0.50, rely=0.30, anchor="center")

label_totalAcum = ctk.CTkLabel(frame_binomial, text="Total acumulado: ", 
                                    width=235, height=45, corner_radius=15, font=("arial", 15))
label_totalAcum.place(rely=0.40, relx=0.5, anchor="center")

tableColumnsBinomial = ['K',"P","P%"]
tableDataBinomial = []

tableBinomial = ttk.Treeview(master=frame_binomial, columns=tableColumnsBinomial, show="headings")
for column in tableColumnsBinomial:
    tableBinomial.heading(column=column, text=column)
    tableBinomial.column(column=column, width=150)

tableBinomial.place(rely=0.65, relx=0.5, anchor="center")

tableBinomial.bind('<Motion>', prevent_resize)
tableBinomial.bind('<<TreeviewSelect>>', acumular)

caminhoImagem = ''
button_gerar_graficobinomial = ctk.CTkButton(frame_binomial, text="Gerar Gráfico", 
                                        width=235, height=45, corner_radius=15, font=("arial", 15), 
                                        command=abrirGraficoBinomial)

# Fim frame binomial
# ----------------------------------------------------------------------------------------------------------------------------------------
# Inicio frame editar dados
label_editar_dados = ctk.CTkLabel(frame_editar_dados, text='Editar dados', font=('arial normal', 24))
label_editar_dados.place(relx=0.5, rely=0.05, anchor="center")

label_titulo_listbox = ctk.CTkLabel(frame_editar_dados, text='Escolha o conjunto de dados', font=('arial normal', 18))
label_titulo_listbox.place(relx=0.5, rely=0.15, anchor="center")

listbox_de_tabelas = CTkListbox(frame_editar_dados, width=550, height=350, command=abrir_top_crud)
listbox_de_tabelas.place(relx=0.5, rely=0.5, anchor="center")

lista_de_tabelas_bd = retornar_tables()
for i, nome_tabela in enumerate(lista_de_tabelas_bd):
    listbox_de_tabelas.insert(i, nome_tabela)
# Fim frame editar dados
# ----------------------------------------------------------------------------------------------------------------------------------------
# Estilo de tema

adicionarElementos(label_login, entry_login, label_senha, entry_senha, button_login, button_cadastrar, switchTheme, tipo=1)
adicionarElementos(button_carregar_dados, button_digitar_dados, button_pareto, button_medidas, button_sair, switchTheme2, button_editar, tipo=2)


if janela._get_appearance_mode() == "light":
    janela._set_appearance_mode("dark")
    frame_main_login._set_appearance_mode("dark")
    frame_main_pricipal._set_appearance_mode("dark")
    frame_menu._set_appearance_mode("dark")
    for element in elementos_login:
        element._set_appearance_mode("dark")
    for element in elementos_principal:
        element._set_appearance_mode("dark")

janela.mainloop()
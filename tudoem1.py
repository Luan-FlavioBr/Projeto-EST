'''
Olá Luan do futuro, você estava na função carregar dados, você tem que colocar o SEGMENTBUTTON e o ScrollableFrame
Boa sorte! >:)
'''

import tkinter as tk
from tkinter import filedialog, PhotoImage, END, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
import os

from DBController import *
from cadastro import *
from conversaoTxt import *
from paretoExel import *


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

    if len(dados_login) == 0:
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


def carregarDados():
    frame_digitar.place(x=700, rely=-0.5, anchor="center")
    frame_carregar.place(x=700, rely=0.5, anchor="center")


def digitarDados():
    frame_carregar.place(x=700, rely=-0.5, anchor="center")
    frame_digitar.place(x=700, rely=0.5, anchor="center")
    frame_analise_pareto.place(x=700, rely=-0.5, anchor="center")


def carregarDados():
    frame_digitar.place(x=700, rely=-0.5, anchor="center")
    frame_carregar.place(x=700, rely=0.5, anchor="center")
    frame_analise_pareto.place(x=700, rely=-0.5, anchor="center")


def analisePareto():
    frame_analise_pareto.place(x=700, rely=0.5, anchor="center")
    frame_digitar.place(x=700, rely=-0.5, anchor="center")
    frame_carregar.place(x=700, rely=-0.5, anchor="center")


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


def escolherCaminhoArquivo():
    janela.focus_set()
    if radio_var.get() != 0:
        origem = filedialog.askopenfilename(initialdir="/Desktop",
                                            title="Abrir exel",
                                            filetypes = (("Arquivos Exel","*.xlsx"), ("Arquivos txt","*.txt")))

        resultado = salvar_no_bd(origem, f'{entry_nome_bd.get()}_{radio_var.get()}')
        
        if resultado == None:
            tela_error("Erro ao salvar conjunto de dados! Siga corretamente a formatação do arquivo selecionado!")
        elif resultado == 'Nome Table Error':
            tela_error("O nome do conjunto de dados já existe!")
        else:
            global tableDataBaseDados
            tableDataBaseDados = retornar_tables_pareto()
            limpar_tabela_bd()
            carregar_tabela_bd()


def salvar_no_bd(origem, nome_do_table):
    entry_nome_bd.delete(0, END)
    tipo_arquivo = origem.split('/')[-1].split(".")[-1]
    
    if tipo_arquivo == "txt":
        if radio_var.get() == 1:
            ...
        elif radio_var.get() == 2:
            lista_de_dados = pegar_dados_qualitativos_txt(origem)
            return inserir_rol_dados_qualitativos(lista_de_dados, nome_do_table)
    elif tipo_arquivo == "xlsx":
        if radio_var.get() == 1:
            ...
        elif radio_var.get() == 2:
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
    inserir_rol_dados_qualitativos(tableData, "teste2")
    tableData = buscar_rol_dados("teste2")
    carregar_tabela()


# Frame Análise Pareto
def gerarAnalise(gerarAnalise):
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
        
        localDoArquivo = operacoesExel(origem, origem, buscar_rol_dados(valor_linha[0]))

        scroll_frame_pareto = ctk.CTkScrollableFrame(top_level)
        scroll_frame_pareto.pack(fill="both", expand=True)

        label_titulo = ctk.CTkLabel(scroll_frame_pareto, text="Tabela de Análise de Pareto", width=200, height=35, font=("calibri bold", 24))
        label_titulo.pack()

        # Fazendo a tabela de análise de pareto
        tableColumns = ['Tipo de falha','Nº de Ocorrências','Fr(%)', 'Fr Acum(%)']

        tablePareto = ttk.Treeview(master=scroll_frame_pareto, columns=tableColumns, show="headings")
        for column in tableColumns:
            tablePareto.heading(column=column, text=column)
            tablePareto.column(column=column, width=150)

        tablePareto.column("Nº de Ocorrências", anchor='e')
        tablePareto.column("Fr(%)", anchor='e')
        tablePareto.column("Fr Acum(%)", anchor='e')

        stylePareto = ttk.Style()
        stylePareto.theme_use('default')
        stylePareto.configure("Treeview.Heading", background="#1F6AA5", foreground="white", font=("arial bold", 15), borderwidth=0, relief = 'flat')
        stylePareto.map("Treeview.Heading", background=[("pressed", "!focus", "#1F6AA5"), ("active", "#1F6AA5"), ("disabled", "white")])

        stylePareto.configure("Treeview", background="#343638", fieldbackground="#242424", foreground="white",
                        corner_radius=15, borderwidth=1)
        
        tableDataPareto = lerarquivo(localDoArquivo)
        
        for rowData in tableDataPareto:
            tablePareto.insert(parent='', index='end', values=rowData)
        
        tablePareto.pack()
        top_level.focus_get()
        
        label_titulo_grafico = ctk.CTkLabel(scroll_frame_pareto, text="Gráfico de Pareto", font=("calibri bold", 24))
        label_titulo_grafico.pack(pady=50) 

        localDaImagem = aplicacaoGraficoPareto(localDoArquivo, gerarAnalise)

        print(localDaImagem)
        my_image = ctk.CTkImage(light_image=Image.open(localDaImagem),
                                  dark_image=Image.open(localDaImagem),
                                  size=(600, 300))

        image_label = ctk.CTkLabel(scroll_frame_pareto, image=my_image, text="").pack()
        

        top_level.grab_set()
        top_level.protocol("WM_DELETE_WINDOW", sair_top)
        
        
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
                                text="Medidas e tabelas", font=font_normal)
button_medidas.place(y=165, x=90, anchor="center")


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

button_inserir_rol_dados = ctk.CTkButton(frame_digitar, width=235, height=45, corner_radius=15,
                                         text="Salvar no banco de dados", command=inserirDados_noBD)
button_inserir_rol_dados.place(relx=0.5, rely=0.85, anchor="center")

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
                                           command=lambda:gerarAnalise(checkbox_gerar_exel.get()))
button_gerar_analisepareto.place(relx=0.5, rely=0.75, anchor="center")

check_var = ctk.StringVar(value=True)
checkbox_gerar_exel = ctk.CTkCheckBox(frame_analise_pareto, text="Gerar arquivo exel",
                           variable=check_var, onvalue=True, offvalue=False)
checkbox_gerar_exel.place(relx=0.5, rely=0.85, anchor="center")

# Fim frame análise pareto
# ----------------------------------------------------------------------------------------------------------------------------------------
# Incio frame medidas e tabelas



# # Fim frame medidas e tabelas
# ----------------------------------------------------------------------------------------------------------------------------------------
# Estilo de tema

adicionarElementos(label_login, entry_login, label_senha, entry_senha, button_login, button_cadastrar, switchTheme, tipo=1)
adicionarElementos(button_carregar_dados, button_digitar_dados, button_pareto, button_medidas, button_sair, switchTheme2, tipo=2)

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
 
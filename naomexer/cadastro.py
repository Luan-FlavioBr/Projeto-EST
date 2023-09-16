import customtkinter as ctk
import sqlite3 as sql
from DBController import *

def tela_cadastrar_starter():

    def cadastrar_user():
        if entry_senha.get() == entry_confirmacao_senha.get():
            try:
                cadastrar_usuario(entry_login.get(), entry_senha.get())
            except sql.IntegrityError as ex:
                print('Login já existente!')
        else:
            print('Senhas não conferem!')
            


    def mudarTema():
        if switchVar.get() == "Dark":
            janela._set_appearance_mode("dark")
        else:
            janela._set_appearance_mode("light")

    janela = ctk.CTk()

    janela.title("Tela Cadastro")
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width/2) - (400/2)
    y = (screen_height/2) - (300/2)

    janela.geometry('%dx%d+%d+%d' % (300, 400, x, y))
    janela._set_appearance_mode('dark')
    janela.resizable(width=False, height=False)

    font_negrito = ('arial bold', 18)

    label_login = ctk.CTkLabel(janela, text="LOGIN", font= font_negrito).place(relx=0.25, y=75, anchor="center")
    entry_login = ctk.CTkEntry(janela, width=210, placeholder_text="Digite seu login")
    entry_login.place(relx=0.5, y=105, anchor="center")

    label_senha = ctk.CTkLabel(janela, text="SENHA", font= font_negrito).place(relx=0.25, y=135, anchor="center")
    entry_senha = ctk.CTkEntry(janela, width=210, placeholder_text="Digite sua senha", show='*')
    entry_senha.place(relx=0.5, y=165, anchor="center") 

    label_confirmacao_senha = ctk.CTkLabel(janela, text="CONFIRME SUA SENHA", font= font_negrito).place(relx=0.49, y=200, anchor="center")
    entry_confirmacao_senha = ctk.CTkEntry(janela, width=210, placeholder_text="Confirme sua senha", show='*')
    entry_confirmacao_senha.place(relx=0.5, y=230, anchor="center")

    button_cadastrar = ctk.CTkButton(janela, width=200, text="Cadastrar!", command=cadastrar_user)
    button_cadastrar.place(relx=0.5, y=270, anchor='center')

    switchVar = ctk.StringVar(value='Dark')
    switchTheme = ctk.CTkSwitch(janela, text="Tema", command=mudarTema, variable=switchVar, onvalue='Dark', offvalue="Light")
    switchTheme.place(relx=0.20, rely=0.90, anchor="center")

    janela.mainloop()
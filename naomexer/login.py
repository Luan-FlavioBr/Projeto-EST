import customtkinter as ctk
import sys

from principal import tela_p_starter
from cadastro import *
from DBController import *


def tela_starter():

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
                janela.quit()
                janela.destroy()
                tela_p_starter()


    def cadastrar_clicado():
        tela_cadastrar_starter()


    def mudarTema():
        if switchVar.get() == "Dark":
            janela._set_appearance_mode("dark")
        else:
            janela._set_appearance_mode("light")


    janela = ctk.CTk()

    janela.title("Tela Login")
    janela.protocol("WM_DELETE_WINDOW", sys.exit)
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width/2) - (400/2)
    y = (screen_height/2) - (300/2)

    janela.geometry('%dx%d+%d+%d' % (300, 400, x, y))
    janela._set_appearance_mode('dark')
    janela.resizable(width=False, height=False)

    font_negrito = ('arial bold', 18)

    label_login = ctk.CTkLabel(janela, text="LOGIN", font= font_negrito).place(relx=0.25, y=100, anchor="center")
    entry_login = ctk.CTkEntry(janela, width=210, placeholder_text="Digite seu login")
    entry_login.place(relx=0.5, y=130, anchor="center")

    label_senha = ctk.CTkLabel(janela, text="SENHA", font= font_negrito).place(relx=0.25, y=168, anchor="center")
    entry_senha = ctk.CTkEntry(janela, width=210, placeholder_text="Digite sua senha", show='*')
    entry_senha.place(relx=0.5, y=198, anchor="center")

    button_login = ctk.CTkButton(janela, width=200, text="Logar", command=login_clicado)
    button_login.place(relx=0.5, y=238, anchor="center")

    button_cadastrar = ctk.CTkButton(janela, width=200, text="Não tem cadastro? Clique aqui!", 
                                     fg_color='transparent', hover_color='#444444', command=cadastrar_clicado)
    button_cadastrar.place(relx=0.5, y=268, anchor="center")

    switchVar = ctk.StringVar(value='Dark')
    switchTheme = ctk.CTkSwitch(janela, text="Tema", command=mudarTema, variable=switchVar, onvalue='Dark', offvalue="Light")
    switchTheme.place(relx=0.20, rely=0.90, anchor="center")

    janela.mainloop()

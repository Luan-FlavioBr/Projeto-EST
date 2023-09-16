import customtkinter as ctk
import sys

from login import *
from DBController import *


def tela_p_starter():

    def mudarTema():
        if switchVar.get() == "Dark":
            janelaPrincipal._set_appearance_mode("dark")
        else:
            janelaPrincipal._set_appearance_mode("light")


    def sair():
        janelaPrincipal.exit()
        tela_starter()

    janelaPrincipal = ctk.CTk()

    janelaPrincipal.protocol("WM_DELETE_WINDOW", sys.exit)
    janelaPrincipal.title("Tela Principal")
    screen_width = janelaPrincipal.winfo_screenwidth()
    screen_height = janelaPrincipal.winfo_screenheight()

    w = 1200
    h = 600

    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)

    janelaPrincipal.geometry('%dx%d+%d+%d' % (w, h, x, y))
    janelaPrincipal._set_appearance_mode('dark')
    janelaPrincipal.resizable(width=False, height=False)

    font_negrito = ('arial bold', 18)
    font_normal = ('arial normal', 15)

    frame_menu = ctk.CTkFrame(janelaPrincipal, width=160, height=600).place(x=0, y=0)


    button_pareto = ctk.CTkButton(frame_menu, width=145, height=35, corner_radius=15, 
                                  text="Análise de Pareto", bg_color="#2B2B2B", font=font_normal)
    button_pareto.place(y=25, x=80, anchor="center")


    button_medidas = ctk.CTkButton(frame_menu, width=145, height=35, corner_radius=15, 
                                  text="Medidas e tabelas", bg_color="#2B2B2B", font=font_normal)
    button_medidas.place(y=75, x=80, anchor="center")


    switchVar = ctk.StringVar(value='Dark')
    switchTheme = ctk.CTkSwitch(janelaPrincipal, text="Tema", command=mudarTema, variable=switchVar, 
                                onvalue='Dark', offvalue="Light", bg_color="#2B2B2B", font=font_normal)
    switchTheme.place(x=80, rely=0.85, anchor="center")


    button_sair = ctk.CTkButton(frame_menu, width=145, height=35, corner_radius=15, 
                                  text="Sair", bg_color="#2B2B2B", font=font_normal, command=sair)
    button_sair.place(rely=0.95, x=80, anchor="center")

    janelaPrincipal.mainloop()


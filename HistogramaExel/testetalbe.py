import customtkinter as ctk
from tkinter import ttk

from medidasDeTendencia import *


janela = ctk.CTk()

# Configurando a janela principal

janela.title("App Teste")
janela.geometry("700x400") # janela.geometry(dimensões)
janela.maxsize(width=700, height=400)
janela.minsize(width=700, height=400)
janela.resizable(width=False, height=False)

# Customizando tema da nossa aplicação = Aula 03

def banana():
    tableData = lerarquivo()
    for rowData in tableData:
        table.insert(parent='', index='end', values=rowData)


tableColumns = ['Tipo de falha','Nº de Ocorrências','Fr(%)', 'Fr Acum(%)']
tableData = []


table = ttk.Treeview(master=janela, columns=tableColumns, show="headings")
for column in tableColumns:
    table.heading(column=column, text=column)
    table.column(column=column, width=150)

table.column("Nº de Ocorrências", anchor='e')
table.column("Fr(%)", anchor='e')
table.column("Fr Acum(%)", anchor='e')

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="#917FB3", fieldbackground="#917FB3", foreground="white")

table.pack()
ctk.CTkButton(janela, command=banana).pack()

janela.mainloop()

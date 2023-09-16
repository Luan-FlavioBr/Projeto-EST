import customtkinter as ctk
from PIL import Image

janela = ctk.CTk()

# Configurando a janela principal
janela.title("App Teste")
janela.geometry("700x400") # janela.geometry(dimensões)
janela.maxsize(width=700, height=400)
janela.minsize(width=700, height=400)
janela.resizable(width=False, height=False)

my_image = ctk.CTkImage(light_image=Image.open("ParetoExelGrafico/GraficoPareto.png"),
                                  dark_image=Image.open("ParetoExelGrafico/GraficoPareto.png"),
                                  size=(500, 300))

image_label = ctk.CTkLabel(janela, image=my_image, text="").pack()

janela.mainloop()
import os
from scipy.stats import binom 
import matplotlib.pyplot as plt


def calcularBinomio(n, p):
    listaValores = list()
    x = range(0,n+1) # valores de x =0,1,2,3 ...
    p_x = binom.pmf(x,n,p) #distribuição dos resultados
    for i,val in enumerate(p_x):
        listaValores.append([i, f'{val:.10f}',f'{val:.2%}'])
    #Grafico
    fig, ax = plt.subplots(figsize=(8, 3.5), dpi=150)
    plt.xlabel('x')
    plt.ylabel('p(x)')
    for a,b in zip(x, p_x):
        plt.text(a-0.5, b-0.0, str(round(b*100,2))+"%", color='black')
    plt.title('Distribuição Binomial')
    plt.bar(x,p_x,width=0.5,color='blue')
    ####
    localScript = os.path.dirname(os.path.abspath(__file__)) if "__file__" in locals() else os.getcwd()
    caminhoImagem = os.path.join(localScript, 'graficoBinomial.png')
    plt.savefig(caminhoImagem, format='png',dpi = 150, bbox_inches = 'tight')

    return listaValores, caminhoImagem

import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from openpyxl.drawing.image import Image
import subprocess

tipo_de_falha = list()
lista = list()

workbook = openpyxl.load_workbook('ParetoExelGrafico/analise.xlsx', data_only = True)
sheet = workbook.active


def pegarExel():
    tipoDefeito = list()
    numeroOcorrencias = list()
    frequecia = list()
    frequeciaAcumulada = list()

    ultimaLinha = 0
    numeroCelula = 2

    while True:
        celula = sheet[f"C{numeroCelula}"].value
        if celula != "Total":
            tipoDefeito.append(celula)
        else:
            ultimaLinha = numeroCelula
            break
        numeroCelula += 1
    
    for numeroOcorrencia in range(2, len(tipoDefeito)+2):
        celula = sheet[f'D{numeroOcorrencia}'].value
        numeroOcorrencias.append(celula)

    for fr in range(2, len(tipoDefeito)+2):
        celula = sheet[f'E{fr}'].value
        frequecia.append(celula * 100)

    for fracum in range(2, len(tipoDefeito)+2):
        celula = sheet[f'F{fracum}'].value
        frequeciaAcumulada.append(celula * 100)


    return tipoDefeito, numeroOcorrencias, frequecia, frequeciaAcumulada, ultimaLinha


tipo_de_falha, numeroOcorrencias, frequencia, frequeciaAcumulada, ultimaLinha = pegarExel()
print(len(tipo_de_falha))
print(len(frequencia))

plt.rcParams.update({'font.size': 14})
df = pd.DataFrame({'tipo defeito' : tipo_de_falha,
                   'Nº Ocor' : numeroOcorrencias, 
                   'freq (%)': frequencia,
                   'cum (%)' : frequeciaAcumulada})

fig,ax1 = plt.subplots(figsize = (12,6))

ax1.set_title('Pareto')

color1 = 'tomato'
#ax1.set_xlabel('X')
ax1.set_ylabel('Nº Ocorrências',color = color1)

bars = ax1.bar(df['tipo defeito'], df['Nº Ocor'],color = color1,edgecolor = 'orange',linewidth = 2,\
                hatch = '*')
#ax1.set_ylim([-10,10])
ax1.tick_params(axis = 'y',labelcolor = color1)

color2 = 'black'
ax2 = ax1.twinx() # compartilhar o mesmo eixo x
ax2.set_ylabel('%',color = color2) 

ax2.plot(df['tipo defeito'], df['cum (%)'],color = color2,marker = 's',markersize = 8, linestyle = '-')

ax2.tick_params(axis = 'y',labelcolor = color2)
ax2.set_ylim([0,120])

for tick in ax1.get_xticklabels():
    tick.set_rotation(90)

for x, y in zip(df['tipo defeito'], df['cum (%)']):
    ax2.annotate(f'{y:.2f}%', xy=(x, y), xytext=(5, -25), textcoords='offset points',
                 ha='center', fontsize=12)

plt.savefig('ParetoExelGrafico/GraficoPareto.png',format='png',dpi = 200, bbox_inches = 'tight')

paretoGrafico = Image('ParetoExelGrafico/GraficoPareto.png')
paretoGrafico.width = 600
paretoGrafico.height = 350

sheet.add_image(paretoGrafico, f"C{ultimaLinha + 3}")

workbook.save('ParetoExelGrafico/analise.xlsx')

subprocess.run(['start', '', 'ParetoExelGrafico/analise.xlsx'], shell=True)
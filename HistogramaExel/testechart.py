import matplotlib.pyplot as plt
from medidasDeTendencia import *

# Dados fornecidos
todasMedidas = list(retornar_dados_tabela_freq())
dados = [(todasMedidas[0][0], todasMedidas[0][-2])]

for i in range(0, len(todasMedidas)):
    if todasMedidas[1][i] != "Totais" and todasMedidas[4][i] != 1:
        dados.append((todasMedidas[1][i], todasMedidas[4][i]))

print(dados)
# Extrai os rótulos e os valores da frequência
rotulos = [item[0] for item in dados[1:]]
valores = [item[1] for item in dados[1:]]

# Remove o primeiro rótulo em branco
rotulos.pop(0)
valores.pop(0)

# Cria o gráfico de barras
plt.bar(rotulos, valores, width=1.0)

# Adiciona rótulos e título
plt.xlabel('Intervalo de Velocidade (MHz)')
plt.ylabel('Frequência (%)')
plt.title('Gráfico de Barras da Frequência de Velocidade')


for i, v in enumerate(valores):
    plt.text(i, v + 0.02, f'{v:.2%}', ha='center', va='bottom', fontsize=10)

# Rotaciona os rótulos do eixo x para facilitar a leitura
plt.xticks(rotation=45, ha='right')

max_freq = max(valores)
plt.ylim(0, max_freq + 0.1)  # Ajuste os limites conforme necessário
plt.gca().set_yticklabels(['{:.0f}%'.format(val * 100) for val in plt.gca().get_yticks()])
# Mostra o gráfico
plt.tight_layout()  # Para evitar que os rótulos fiquem cortados
plt.savefig('HistogramaExel/histograma.png',format='png',dpi = 600, bbox_inches = 'tight')
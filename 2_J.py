# J. Gráfico comparativo entre o grau dos cursos (Bacharelado, Licenciatura, Tecnologia, etc) pelas Notas Integral de Cotas.

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')
df_filtrado = df[['grau', 'nota_integral_cotas']]

media_notas_cotas = df_filtrado.groupby('grau')['nota_integral_cotas'].mean()

fig, ax = plt.subplots(figsize=(8, 6))

barras = ax.bar(media_notas_cotas.index, media_notas_cotas.values)

for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura:.2f}', xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

ax.set_xlabel('Grau dos Cursos')
ax.set_ylabel('Média das Notas de Cotas')
ax.set_title('Comparativo entre Grau dos Cursos e Notas de Cotas')

plt.show()
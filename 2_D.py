# D. Agrupe os dados por Estado e obtenha a média de notas de corte por Estado.

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')

media_notas_estado = df.groupby('uf_busca')['nota_integral_ampla'].mean()

print("Média das notas de corte por Estado:")
print(media_notas_estado)
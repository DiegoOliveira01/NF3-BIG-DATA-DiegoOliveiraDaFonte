# D. Agrupe os dados por Estado e obtenha a média de notas de corte por Estado.

import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/cursos-prouni.csv'

df = pd.read_csv(url, sep=',', encoding = 'utf-8')

media_notas_estado = df.groupby('uf_busca')['nota_integral_ampla'].mean()

print("Média das notas de corte por Estado:")
print(media_notas_estado)
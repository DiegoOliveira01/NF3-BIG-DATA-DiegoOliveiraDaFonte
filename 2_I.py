# I. Estatística Descritiva das Notas Integral Ampla dos cursos de Bacharelado.

import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/cursos-prouni.csv'

df = pd.read_csv(url, sep=',', encoding = 'utf-8')

df_bacharelado_integral = df[(df['turno'] == 'Integral') & (df['grau'] == 'Bacharelado')]

estatisticas_descritivas = df_bacharelado_integral['nota_integral_ampla'].describe()

print("Estatística Descritiva das Notas Integral Ampla dos cursos de Bacharelado:")
print(estatisticas_descritivas)
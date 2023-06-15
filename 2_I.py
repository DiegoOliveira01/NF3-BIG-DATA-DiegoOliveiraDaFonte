# I. Estatística Descritiva das Notas Integral Ampla dos cursos de Bacharelado.

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')

df_bacharelado_integral = df[(df['turno'] == 'Integral') & (df['grau'] == 'Bacharelado')]

estatisticas_descritivas = df_bacharelado_integral['nota_integral_ampla'].describe()

print("Estatística Descritiva das Notas Integral Ampla dos cursos de Bacharelado:")
print(estatisticas_descritivas)
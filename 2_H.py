# H. Média das notas de corte dos cursos de tempo integral.

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')

df_tempo_integral = df[df['turno'] == 'Integral']

media_notas_corte = df_tempo_integral['nota_integral_ampla'].mean()

print(f"A média das notas de corte dos cursos em tempo integral é: {media_notas_corte:.2f}")
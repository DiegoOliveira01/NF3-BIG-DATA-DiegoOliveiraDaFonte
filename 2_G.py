# G. Apresente a média das mensalidades dos cursos de Medicina.

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')

df_medicina = df[df['curso_busca'] == 'Medicina']

media_mensalidades = df_medicina['mensalidade'].mean()

print(f"A média das mensalidades dos cursos de Medicina é: R$ {media_mensalidades:.2f}")
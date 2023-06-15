# C. Agrupe os dados pelos cursos de Matemática, Medicina e Pedagogia.

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')

grupos_desejados = ['Matemática', 'Medicina', 'Pedagogia']

df_filtrado = df[df['curso_busca'].isin(grupos_desejados)]

grupo_grau = df_filtrado.groupby('curso_busca')

contagem_grau = grupo_grau.size()

print(contagem_grau)
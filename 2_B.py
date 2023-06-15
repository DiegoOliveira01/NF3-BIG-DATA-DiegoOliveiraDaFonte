# B. Agrupe os dados pelo grau (Bacharelado, Licenciatura, etc)

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')

grupo_grau = df.groupby('grau')
contagem_grau = grupo_grau.size()
contagem_grau
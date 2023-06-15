# A. Efetuar a limpeza das colunas de notas: onde tiver NaN (Not a Number), substituir por 0,0

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')

df = df.fillna(0)
df
# F. Elimine a coluna “cidade_filtro” do dataframe

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')
df_sem_cidade = df.drop('cidade_filtro', axis=1)

print("Dataframe sem a coluna 'cidade_filtro':")
print(df_sem_cidade)
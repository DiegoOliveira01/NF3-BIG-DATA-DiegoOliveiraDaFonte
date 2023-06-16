# F. Elimine a coluna “cidade_filtro” do dataframe

import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/cursos-prouni.csv'

df = pd.read_csv(url, sep=',', encoding = 'utf-8')
df_sem_cidade = df.drop('cidade_filtro', axis=1)

print("Dataframe sem a coluna 'cidade_filtro':")
print(df_sem_cidade)
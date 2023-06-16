# B. Agrupe os dados pelo grau (Bacharelado, Licenciatura, etc)

import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/cursos-prouni.csv'

df = pd.read_csv(url, sep=',', encoding = 'utf-8')

grupo_grau = df.groupby('grau')
contagem_grau = grupo_grau.size()
contagem_grau
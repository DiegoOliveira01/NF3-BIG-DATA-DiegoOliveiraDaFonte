# A. Efetuar a limpeza das colunas de notas: onde tiver NaN (Not a Number), substituir por 0,0

import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/cursos-prouni.csv'

df = pd.read_csv(url)

df = df.fillna(0)
df
# B. Agrupe os dados por Região e por Ano;
import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/world_alcohol.csv'

data = pd.read_csv(url)

grupo_regiao_ano = data.groupby(['WHO region', 'Year']).size()

print(grupo_regiao_ano)
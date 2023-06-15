# A. Agrupe os dados por tipo de bebidas;
import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/world_alcohol.csv'

data = pd.read_csv(url)

grupo_bebidas = data.groupby('Beverage Types').size()

print(grupo_bebidas)
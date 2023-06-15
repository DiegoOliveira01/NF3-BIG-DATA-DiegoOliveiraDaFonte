# E. Mostre resultados de acordo com alguns critérios:
# i. Mostrar a coluna de bebidas do ano de 1985.
# ii. Mostrar a coluna de Região com valores acima de 4
import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/world_alcohol.csv'

data = pd.read_csv(url)

bebidas_1985 = data[data['Year'] == 1985]['Beverage Types']
print("Coluna de bebidas do ano de 1985:")
print(bebidas_1985)

regioes_acima_4 = data[data['Display Value'] > 4]['WHO region']
print("\nColuna de Região com valores acima de 4:")
print(regioes_acima_4)
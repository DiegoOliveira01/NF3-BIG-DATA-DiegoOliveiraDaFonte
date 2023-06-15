# C. Seção de Contagens: Contar a ocorrência de Regiões, de Países e a soma da coluna de valores por Bebida.
import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/world_alcohol.csv'

data = pd.read_csv(url)

contagem_regioes = data['WHO region'].value_counts()

contagem_paises = data['Country'].value_counts()

soma_valores_bebida = data.groupby('Beverage Types')['Display Value'].sum()

print("Contagem de ocorrência de regiões:")
print(contagem_regioes)
print("\nContagem de ocorrência de países:")
print(contagem_paises)
print("\nSoma da coluna de valores por bebida:")
print(soma_valores_bebida)
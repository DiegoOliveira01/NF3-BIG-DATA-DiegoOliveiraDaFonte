# D. Realize análises estatísticas da coluna dos valores: Média, Moda, Mediana, Estatística Descritiva e Gráfico de comparação dos valores agrupados por tipo de bebida.
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/world_alcohol.csv'

data = pd.read_csv(url)

media = data['Display Value'].mean()
moda = data['Display Value'].mode().values
mediana = data['Display Value'].median()
descritiva = data['Display Value'].describe()

agrupado_bebida = data.groupby('Beverage Types')['Display Value'].sum()
agrupado_bebida.plot(kind='bar')
plt.xlabel('Tipo de Bebida')
plt.ylabel('Soma dos Valores')
plt.title('Comparação dos Valores por Tipo de Bebida')
plt.show()

print("Análises estatísticas da coluna 'Display Value':")
print("Média:", media)
print("Moda:", moda)
print("Mediana:", mediana)
print("Estatística Descritiva:")
print(descritiva)
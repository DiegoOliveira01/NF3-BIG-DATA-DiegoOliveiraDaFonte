# G. Apresente a média das mensalidades dos cursos de Medicina.

import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/cursos-prouni.csv'

df = pd.read_csv(url, sep=',', encoding = 'utf-8')

df_medicina = df[df['curso_busca'] == 'Medicina']

media_mensalidades = df_medicina['mensalidade'].mean()

print(f"A média das mensalidades dos cursos de Medicina é: R$ {media_mensalidades:.2f}")
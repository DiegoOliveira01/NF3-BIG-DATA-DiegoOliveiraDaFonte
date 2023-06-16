# E. Agrupe os dados pelos cursos Tecnológicos

import pandas as pd

url = 'https://raw.githubusercontent.com/DiegoOliveira01/NF3-BIG-DATA-DiegoOliveiraDaFonte/main/cursos-prouni.csv'

df = pd.read_csv(url, sep=',', encoding = 'utf-8')

cursos_tecnologicos = df[df['grau'] == 'Tecnológico']
cursos_tecnologicos
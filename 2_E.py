# E. Agrupe os dados pelos cursos Tecnológicos

import pandas as pd

df = pd.read_csv('cursos-prouni.csv', sep=',', encoding = 'utf-8')

cursos_tecnologicos = df[df['grau'] == 'Tecnológico']
cursos_tecnologicos
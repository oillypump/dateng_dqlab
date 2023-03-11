import pandas as pd

data = pd.DataFrame({
    'kelas': 6*['A'] + 6*['B'],
    'murid': 2*['A1'] + 6*['A2'] 2*['A3'] + 2*['B1'] + 2*['B2'] + 2*['B3'],
    'pelajaran': 6*['math','english'],
    'nilai': [90,60,70,85,50,60,100,40,95,80,60,45]
}, columns=['kelas','murid','pelajaran','nilai'])

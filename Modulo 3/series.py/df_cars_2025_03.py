import pandas as pd

carros = pd.read_csv('2025.csv')

formato = carros.describe()
print(formato)



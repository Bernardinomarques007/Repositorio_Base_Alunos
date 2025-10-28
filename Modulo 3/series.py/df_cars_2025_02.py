import pandas as pd

carros = pd.read_csv('2025.csv')


média = carros['year'].mean()
print(f'A média dos anos de fabricação é: {média}')
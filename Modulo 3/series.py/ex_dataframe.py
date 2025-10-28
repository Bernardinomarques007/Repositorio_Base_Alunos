import pandas as pd

carros = pd.read_excel('Car2DB_eng_cut.xlsx')

print(carros)

média = carros['Year from (Generation)'].mean()
print(média)

descrição = carros.describe()
print(descrição)

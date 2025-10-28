import pandas as pd

print('Criando uma instância de series a partir de uma lista numérica')

titulos_gerais = pd.Series([1920, 1926, 1927, 1932, 1933, 1934, 1936, 1940, 1942, 1944, 1947, 1950, 1951, 1959, 1960, 1963, 1966, 1967, 1967,
1969, 1972, 1973, 1974, 1976, 1993, 1994, 1996, 1998, 1999, 2008, 2012, 2015, 2016, 2018, 2020, 2020, 2020, 2021, 2022, 2022, 2023, 2023, 2024])

print("O Palmeiras é o maior camp~eao nacional com 77 titulos")
print(titulos_gerais)
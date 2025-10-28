import pandas as pd

s = pd.Series([ 'Wes McKinney', 'Criador do pandas'],
              index=['Pessoa', 'Quem'])
print('Criando uma série a partir de uma lista de valores e outras de rótulos: ')
print(s)
print(f'Tipo de variavel: {type(s)}')
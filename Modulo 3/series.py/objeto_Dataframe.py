import pandas as pd

dados = {
    'nome': ['v-rod', 'hayabusa'],
    'ano': [2001, 1999],
    'cc': [1250, 1340 ],
    'marca': ['harley-davidson', 'Suzuki']
}

df_dados = pd.DataFrame(dados)

print("--- DatraFrame ---")
print(dados)

descrição = df_dados.describe()
print(descrição)

media = df_dados['cc'].mean()
print(f"a media das cc das motos é {media}")


import pandas as pd
import glob

arquivos = glob.glob("dados/entrada/*.xlsx")

lista_dfs = []

for arquivo in arquivos:
    df = pd.read_excel(arquivo)
    lista_dfs.append(df)

df_consolidado = pd.concat(lista_dfs)

print(df_consolidado.shape)
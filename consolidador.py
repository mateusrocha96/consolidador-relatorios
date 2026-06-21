import pandas as pd
import glob

arquivos = glob.glob("dados/entrada/*.xlsx")

lista_dfs = []

for arquivo in arquivos:
    df = pd.read_excel(arquivo)
    lista_dfs.append(df)

df_consolidado = pd.concat(lista_dfs)

print(df_consolidado.shape)
resultado = df_consolidado.groupby(["Região", "Produto"])["Qtd Vendas"].sum()
print(resultado)
resultado.to_excel("saida/relatorio_consolidado.xlsx")
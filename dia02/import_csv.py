#%%
import pandas as pd
#%%
# Usa-se o ".." para subir uma pasta e poder acessar a pasta Data na origem

df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers
# %%
# Descobrindo quantas colunas e linhas temos no DataFrame

df_customers.shape

# %%
# Informação de quanto esse dataset está ocupando na memória

df_customers.info(memory_usage='deep')
# %%
# Estatística descritiva da coluna "Points"

df_customers["Points"].describe()

# %%
# Convertendo a coluna Points de object para int

df_customers["Points"].astype(int)
#%%
condicao = df_customers["Points"] > 1000
df_customers[condicao]


# %%
# Descobrindo quem tem o máximo de pontos

maximo = df_customers["Points"].max()
condicao = df_customers["Points"] == maximo
df_customers[condicao]

# %%
# Refatorando o máximo_1
condicao = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]

# %%
# Refatorando o máximo_2
df_customers[df_customers["Points"] == df_customers["Points"].max()]

# %%
# Filtrando pelo nome o código acima

df_customers[df_customers["Points"] == df_customers["Points"].max()]["Name"]

# %%
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]

# %%
# Buscando usuários que estão entre 1000 e 2000 Pontos

condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_1000_2000 = df_customers[condicao].copy()

df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000
# %%
# Selecionando mais de uma coluna no DataFrame, usa-se [[,]]
df_customers[["UUID", "Name"]]

#%%
df_customers.columns

# %%
colunas = df_customers.columns.tolist()
colunas.sort()

df_customers[colunas]
df_customers
# %%
# Renomeando colunas do DataFrame
df_customers.rename(columns={"UUID": "Id",
                             "Name": "Nome",
                             "Points": "Pontos"},
                             inplace=True
                             )
df_customers

# %%

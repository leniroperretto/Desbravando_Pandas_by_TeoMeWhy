# %%
import pandas as pd
# %%
# Criando um DataFrame

data = {
    "Name": ["Tom", "Nick", "Krish", "Jack"],
    "LastName" : ["Smith", "Brown", "Miller", "Williams"],
    "Age": [20, 21, 19, 18],
}

#%%
# Acessando o primeiro elemento da lista de "Age"

data["Age"][0]
# %%

df = pd.DataFrame(data)
df

# %%
# Navegando por meio do iloc no DataFrame

df["Age"].iloc[0]

# %%
df["LastName"].iloc[0]

# %%

type(df.iloc[0])
# %%

df["Age"]
# %%

df.index=[3,2,1,0]
df
# %%

df["Age"].iloc[0]
# %%
# Verificando as colunas do DataFrame

df.columns
# %%

df.info(memory_usage='deep')
# %%

df.describe()
# %%

df['peso'] = [80, 53, 65, 14]

sumario = df.describe()

sumario['peso']['mean']

# %%
# Observando as duas primeiras linhas

df.head(2)
# %%
# Observando as duas últimas linhas

df.tail(2)
# %%

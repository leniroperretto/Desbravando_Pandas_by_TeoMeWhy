#%%
import pandas as pd
# %%
data_user = {
    "id": [1, 2, 3, 4, 5],
    "name": ["John", "Anna", "Peter", "Linda", "Bob"],
    "age": [28, 24, 35, 32, 40],
}

df_user = pd.DataFrame(data_user)
df_user
# %%
data_transacoes = {
    "id_user": [1, 1, 1, 2, 3, 3],
    "vl": [432, 532, 123, 6, 4, 87],
    "qtProdutos": [2, 1, 3, 6, 10, 2]
}

df_transacao = pd.DataFrame(data_transacoes)
df_transacao
# %%

df_transacao.merge(df_user, 
                   #how="left",
                   how="inner",
                   #how="right", 
                   left_on="id_user", 
                   right_on="id")

# %%
df_merge = df_transacao.merge(df_user, 
                   #how="left",
                   #how="inner",
                   how="left", 
                   left_on="id_user", 
                   right_on="id")
# %%

df_merge[df_merge["name"].isna()]
# %%

#%%
import pandas as pd
# %%

data = {
    "Nome": ["Tom", "Nick", "Krish", "Jack", "Tom", "Jacob"],
    "Idade":[32, 33, 2, 33, 32, 25],
    "updated_at":[1, 2, 3, 1, 2, 3]
}
#%%

df = pd.DataFrame(data)

df = df.sort_values(by="updated_at", ascending=True)
df
# %%
# Removendo duplicadas
df = df.drop_duplicates(subset=["Nome", "Idade"], keep="first")
df

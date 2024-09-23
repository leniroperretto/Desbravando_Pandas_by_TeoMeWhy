#%% 
import pandas as pd
import numpy as np
# %%
data = {
    "nome": ["João", "Maria", "José", "Helena", "Pedro"], 
    "idade": [31, 32, 14, 25, np.nan],
    "renda": [np.nan, 3245, 357, 12432, np.nan],
}
# %%
df = pd.DataFrame(data)
df
# %%
df["idade"].isna().sum()
# %%
df.isna().sum()
# %%
# Para a idade, pegar a média da idade e colocar aonde tem o item NaN
# Para a renda, pegar a média da randa e colocar aonde tem o item NaN

df.fillna({"idade": df["idade"].mean(),
           "renda": df["renda"].mean()})
# %%
df
df.dropna(how="all") # usa-se o how="all" para que o programa apenas remova todos os critérios das linha com NaN
df.dropna(subset=["idade", "renda"], how="all") #aqui setamos a coluna no qual queremos dropar os NaN
df.dropna(subset=["idade", "renda"], how="any") #aqui setamos a coluna no qual queremos dropar os NaN, ao menos uma coluna tem que ter essa condição
# %%
# removendo NaN por coluna
df.dropna(axis=1, how='all')
# %%

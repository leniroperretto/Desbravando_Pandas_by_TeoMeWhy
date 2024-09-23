#%%
import pandas as pd
# %%

data_01 = {
    "id": [1, 2, 3, 4],
    "name": ["John", "Anna", "Peter", "Linda"],
    "age": [28, 24, 35, 32],
}

df_01 = pd.DataFrame(data_01)
df_01

#%%

data_02 = {
    "id": [5, 6, 7, 8],
    "name": ["Ellie", "Bob", "Mary", "Petter"],
    "age": [23, 33, 19, 21],
}

df_02 = pd.DataFrame(data_02)
df_02

# %%

pd.concat([df_01, df_02]).reset_index(drop=True)

# %%

data_03 = {
    "sobrenome": ["Smith", "Thompson", "White", "Saint"],
    "renda": [3100, 3150, 3050, 3200 ]
}

df_03 = pd.DataFrame(data_03).sort_values(["renda", "sobrenome"], ascending=[False, True])
df_03
# %%

pd.concat([df_01, df_03], axis=1)
# %%

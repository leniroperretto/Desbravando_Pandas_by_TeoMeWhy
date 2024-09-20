# %% 
import pandas as pd

#%%
# Simular e filtar os usuários que tiveram transações com 30 dias ou mais
df = pd.read_excel("../data/transactions.xlsx")
df
# %%

df_last = (df.sort_values("DtTransaction", ascending=False)
      .drop_duplicates(subset=["IdCustomer"], keep="first")
)
df_last["IdCustomer"].nunique()
# %%

condicao = df["IdCustomer"] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]
# %%

df_last[df_last["IdCustomer"] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']
# %%

# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df.head()
#%%
colunas = ["UUID", "Points", "IdCustomer", "DtTransaction"]

df[colunas].head()
# %%
df.info(memory_usage='deep')
# %%

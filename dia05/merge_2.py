#%%
import pandas as pd
#%%
# Importando a planilha de customers
df_customer = pd.read_csv("../data/customers.csv", sep=";")
df_customer
# %%
# Importando a planilha de transactions
df_transactions = pd.read_excel("../data/transactions.xlsx")
df_transactions

#%%
# Importando a planilha de transactions_products
df_transactions_product = pd.read_parquet("../data/transactions_cart.parquet")
df_transactions_product
# %%
# Realizando o merge de 2 planilhas
df_join = df_transactions.merge(df_customer,
                      how="left",
                      left_on="IdCustomer",
                      right_on="UUID",
                      suffixes=("_transacao", "_cliente"))

df_join

# %%
df_join.merge(df_transactions_product,
              how="inner",
              left_on="UUID_transacao",
              right_on="IdTransaction")
# %%
df_join = (df_transactions.merge(df_customer,
                                how="left",
                                left_on="IdCustomer",
                                right_on="UUID",
                                suffixes=("_transacao", "_cliente"))
                        .merge(df_transactions_product,
                                how="inner",
                                left_on="UUID_transacao",
                                right_on="IdTransaction"))

df_join
# %%

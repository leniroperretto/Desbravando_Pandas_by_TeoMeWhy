#%%

import pandas as pd
import sqlalchemy
# %%

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

# %%

df_transctions_cart = pd.read_sql_table("transactions_cart", engine)
df_transctions_cart
# %%

query = '''SELECT * 
    FROM customers AS t1
    LEFT JOIN transactions AS t2
    ON t1.UUID = t2.IdCustomer
    LIMIT 10'''

df_join = pd.read_sql_query(query, engine)
df_join
# %%

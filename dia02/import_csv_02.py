# %%
import pandas as pd

df = pd.read_csv("../data/products.csv", 
                 sep=";",
                 names=["Id", "Name", "Description"])
df
# %%
# Renomeando as colunas
df.rename(columns={"Name":"Nome", "Description":"Descrição"})   

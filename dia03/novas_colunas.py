# %%
import pandas as pd
import numpy as np
# %%

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df["Points_double"] = df["Points"] * 2
df
# %%

df["Points_ratio"] = df["Points_double"] / df["Points"]
df
# %%

df["Constante"] = None
df
# %%

df["Points_log"] = np.log(df["Points"])
df
# %%

np.log(df[["Points", "Points_double", "Points_ratio"]])
# %%
# Criando uma coluna e colocando os nomes em UPPER
nomes_alta = []
for i in df["Name"]:
    nomes_alta.append(i.upper())

df["Nome_Alta"] = nomes_alta
df

# %%

df["Name"].str.upper()
# %%
# criando uma função
def get_first(nome:str):
    return nome.split("_")[0]
# %%

get_first('Teo_calvo')
# %%
# .apply vai aplicar a função em todas as linhas da série
df["Name"].apply(get_first)
df
# %%
# criando uma função lambda
# get_f = lambda x,y: x + y
get_f = lambda nome: nome.split("_")[0]
get_f("Téo")
# %%

def intervalo_pontos(pontos):
    if pontos < 2500:
        return "Baixo"
    elif pontos < 3500:
        return "Medio"
    else:
        return "Alto"
    
df["Faixa_Pontos"] = df["Points"].apply(intervalo_pontos)
df
# %%

df["UUID"].apply(lambda x: x[-3:])
# %%

data = {
    "nome": ["João", "Maria", "José", "Cláudia"],
    "recência": [1, 30, 10, 45],
    "valor": [100, 2000, 15, 500],
    "frequencia": [2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)

def rfv(row):
    nota = 0
    
    if row['recência'] <= 10:
        nota += 10
    elif 10 < row['recência'] <= 30:
        nota += 5
    elif row['recência'] > 30:
        nota += 0

    if row['valor'] > 1000:
        nota += 10
    elif 100 <= row['valor'] < 1000:
        nota += 5
    elif row['valor'] < 100:
        nota += 0

    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota += 5
    elif row['frequencia'] < 5:
        nota += 0
        
    return nota


# %%

df_crm["RFV"] = df_crm.apply(rfv, axis=1)
df_crm
# %%

df_crm.iloc[0]
# %%

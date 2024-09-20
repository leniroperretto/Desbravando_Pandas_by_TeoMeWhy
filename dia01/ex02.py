# Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome
 
# dados = {"nome": ["João", "Maria", "José"], "idade": [31, 32, 14]}
 
 #%%
 
import pandas as pd
# %%
# Converta o seguinte dicionário para DataFrame

dados = {"nome": ["João", "Maria", "José"], "idade": [31, 32, 14]}
df = pd.DataFrame(dados)
df

# %%
# Sumário de coluna numerico

sumario_numericas = df.describe()
sumario_numericas
#%%
# Sumário de coluna numerico

sumario_texto = df["nome"].describe()
sumario_texto
# %%
# Média da coluna idade

df["idade"].mean()
# %%
# Último nome da coluna nome

df["nome"].iloc[-1]
#%%
import pandas as pd

#%%
idades = [30, 42, 90, 34]
idades
# %%
# media das idades
media = sum(idades) / len(idades)

# variancia
total = 0

for i in idades:
    total += (media - i) ** 2

variancia = total / (len(idades) -1)
variancia
#%%
# Transformação para séries Pandas
series_idades = pd.Series(idades)
series_idades

# %%
# Métodos da séries Pandas
# Média
series_idades.mean()
# %%
# Variância
series_idades.var()

# Desvio padrão
series_idades.std()

# %%
# Mediana
series_idades.median()

# %%
# 3º Quartil
series_idades.quantile(0.75)

# %%
# Sumarização
series_idades.describe()

# %%
# Dimensão da série
series_idades.shape

# %%
# Navegando na Lista
idades[3] #localizando no índice 0

# %%
# Navegando na Série
series_idades[2]

# %%
# Alterando index da Série
series_idades.index = ['l', 'e', 'n', 'i']

# %%
# Navegando nos índices novos
series_idades['n']

# %%
# Usa-se o iloc para buscar a posição do item
# Usa-se o loc para buscar pelo índice
series_idades.iloc[2:4]
# %%

series_idades.iloc[0:2]
# %%
series_idades.name = 'idades'
series_idades
# %%
series_idades = pd.Series(idades, name="idades")
series_idades
# %%

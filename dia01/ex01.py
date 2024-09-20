# Converta a seguinte lista de dados para uma Series Pandas e obtenha:
# Média
# Desvio Padrão
# Máximo Valor

# Os dados são:
# dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

#%%
import pandas as pd

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
series = pd.Series(dados)
series
# %%

#  Média
media = series.mean()
media

# %%

# Desvio Padrão

desvio = series.std()
desvio
# %%

# Máximo Valor

maximo = series.max()
maximo
# %%

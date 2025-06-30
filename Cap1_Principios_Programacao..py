# %% [markdown]
# # Capítulo 1 - Princípios de Programação
# ## 1.2 Operações no Console
2 + 3 * (4 ** 2)  # Exemplo de precedência de operadores

# %% [markdown]
# ## 1.3 Listas
acoes_ibov = ['PETR4', 'VALE3', 'ITUB4']
print(acoes_ibov[0:2])  # Slicing

# %% [markdown]
# ## 1.5 Estatísticas Básicas
from statistics import mean, stdev
retornos = [0.02, -0.01, 0.03, 0.015]
print(f"Média: {mean(retornos):.2%}")

# %% [markdown]
# ## 1.11 Arrays NumPy
import numpy as np
precos = np.array([45.2, 46.1, 44.9])
variacao = np.diff(precos) / precos[:-1]  # Retornos
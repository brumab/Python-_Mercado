# %% [markdown]
# # CAPÍTULO 6 - Trabalhando com Arrays
# ## 6.5 Estatísticas com Arrays

import numpy as np

# Dados de 3 ativos (PETR4, VALE3, ITUB4)
retornos = np.array([
    [0.02, 0.01, 0.015],  # Dia 1
    [-0.01, 0.03, 0.008],  # Dia 2
    [0.015, -0.02, 0.01]   # Dia 3
])

# Cálculos vetorizados
media = np.mean(retornos, axis=0)
volatilidade = np.std(retornos, axis=0)
correlacao = np.corrcoef(retornos.T)

print(f"Média dos ativos: {media.round(4)}")
print(f"Volatilidade: {volatilidade.round(4)}")
print("\nMatriz de correlação:")
print(correlacao.round(2))
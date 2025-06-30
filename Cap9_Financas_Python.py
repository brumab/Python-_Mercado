# %% [markdown]
# # CAPÍTULO 9 - Finanças e Python
# ## 9.3 Fronteira Eficiente (Markowitz)
import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Dados históricos (retornos diários em %)
retornos = pd.DataFrame({
    'PETR4': [1.2, -0.5, 2.3, 0.7],
    'VALE3': [0.8, 1.5, -1.2, 0.3],
    'ITUB4': [0.5, 0.3, 0.9, 0.4]
})

cov_matrix = retornos.cov() * 252  # Anualização
retornos_medios = retornos.mean() * 252

# Função para minimizar a volatilidade
def portfolio_volatility(weights):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# Otimização
cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0,1) for _ in range(3))
result = minimize(portfolio_volatility, x0=[0.3,0.3,0.4],
                 bounds=bounds, constraints=cons)

print("Pesos ótimos:", np.round(result.x, 3))
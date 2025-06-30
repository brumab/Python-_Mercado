# %% [markdown]
# # CAPÍTULO 7 - Datas e Tempos
# ## 7.3 Formatando Datas em Gráficos

import pandas as pd
import numpy as np  # Esta linha estava faltando!
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Criar série temporal fictícia (B3)
dias = pd.date_range('2023-01-01', periods=90, freq='D')
precos = np.cumsum(np.random.normal(0.001, 0.02, len(dias))) + 100

# Configuração profissional para gráficos
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(dias, precos)

# Formatação de eixos
date_format = DateFormatter("%b-%Y")
ax.xaxis.set_major_formatter(date_format)
ax.set_title("Série Temporal - Preço Teórico", fontsize=14)
ax.set_ylabel("Preço (R$)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
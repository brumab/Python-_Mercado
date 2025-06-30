# Importações obrigatórias no início do arquivo
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Gerar dados financeiros sintéticos (substitua por seus dados reais)
np.random.seed(42)
retornos = np.random.normal(loc=0.001, scale=0.02, size=1000)
volatilidade = np.random.uniform(0.01, 0.05, 100)
retorno = np.random.normal(0.0015, 0.002, 100)
sharpe = retorno / volatilidade

# 2. Gráfico KDE (4.4) - Forma moderna
plt.figure(figsize=(10, 6))
sns.kdeplot(data=retornos, fill=True)  # 'shade' foi substituído por 'fill'
plt.title("Densidade de Retornos Diários", fontsize=14)
plt.xlabel("Retorno (%)", fontsize=12)
plt.ylabel("Densidade", fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# 3. Gráfico 3D (4.6) - Fronteira Eficiente
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot 3D profissional
scatter = ax.scatter(
    volatilidade,
    retorno,
    sharpe,
    c=sharpe,
    cmap='viridis',
    s=50,
    alpha=0.8
)

# Configurações de eixos
ax.set_xlabel('Volatilidade', fontsize=12)
ax.set_ylabel('Retorno', fontsize=12)
ax.set_zlabel('Índice Sharpe', fontsize=12)
ax.set_title('Relação Risco-Retorno-Sharpe', fontsize=16)

# Barra de cores
cbar = fig.colorbar(scatter, shrink=0.7)
cbar.set_label('Sharpe Ratio', fontsize=12)

plt.tight_layout()
plt.show()
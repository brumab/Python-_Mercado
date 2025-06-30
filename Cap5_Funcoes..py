# %% [markdown]
# # CAPÍTULO 5 - Funções em Python
# ## 5.1 Funções Básicas para Análise Financeira

def calcular_retornos(precos):
    """Calcula retornos percentuais diários"""
    return precos.pct_change().dropna()

def media_movel(dados, janela=20):
    """Calcula média móvel simples"""
    return dados.rolling(window=janela).mean()

# Exemplo com dados da B3
import pandas as pd
precos = pd.Series([45.2, 46.1, 44.9, 47.3, 48.0])
retornos = calcular_retornos(precos)
mm20 = media_movel(precos, 20)

print(f"Retornos: \n{retornos}\n")
print(f"Média Móvel 20 períodos: \n{mm20}")
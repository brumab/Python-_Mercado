# Importações essenciais
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 8.2 Criação de DataFrame
print("\n=== 8.2 Criando DataFrame ===")
df = pd.DataFrame({
    'Ação': ['PETR4', 'VALE3', 'BBDC4', 'ITUB4', 'BBAS3'],
    'Preço': [32.15, 68.40, 19.75, 22.60, 34.20],
    'Volume': [5000000, 3500000, 2800000, 4200000, 3100000]
})
print("DataFrame Original:")
print(df)

# 8.10 Cálculos Financeiros
print("\n=== 8.10 Análise Financeira ===")

# Simular série temporal (20 dias úteis)
np.random.seed(42)
dias = 20
historico_precos = pd.DataFrame({
    'PETR4': np.cumprod(1 + np.random.normal(0.001, 0.02, dias)) * 32.15,
    'VALE3': np.cumprod(1 + np.random.normal(0.0008, 0.018, dias)) * 68.40
})

# Calcular retornos e médias móveis
historico_precos['Data'] = pd.date_range(start='2023-01-01', periods=dias)
historico_precos.set_index('Data', inplace=True)

# Adicionar cálculos financeiros
for acao in ['PETR4', 'VALE3']:
    historico_precos[f'Retorno_{acao}'] = historico_precos[acao].pct_change()
    historico_precos[f'MM20_{acao}'] = historico_precos[acao].rolling(5).mean()  # MM5 para exemplo

# Visualização
print("\nÚltimos 5 dias de negociação:")
print(historico_precos.tail())

# Gráfico profissional
plt.figure(figsize=(12, 6))
historico_precos[['PETR4', 'VALE3']].plot(title='Histórico de Preços - Jan/2023', grid=True)
plt.ylabel('Preço (R$)')
plt.xlabel('Data')
plt.tight_layout()
plt.show()

# Análise estatística
print("\nEstatísticas Descritivas:")
print(historico_precos[['Retorno_PETR4', 'Retorno_VALE3']].describe())
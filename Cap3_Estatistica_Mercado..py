# Verificação de imports
try:
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy.stats import norm
    print("→ Bibliotecas carregadas com sucesso!")
except ImportError as e:
    print(f"Erro: {e}\nExecute no PowerShell:\npip install seaborn scipy statsmodels pandas matplotlib numpy")
    exit()

# Dados de exemplo (retornos diários em %)
retornos = np.random.normal(loc=0.001, scale=0.02, size=1000)

# Análise estatística
print("\n=== Análise Estatística ===")
print(f"Média: {np.mean(retornos):.4f}")
print(f"Desvio Padrão: {np.std(retornos):.4f}")
print(f"Probabilidade de retorno ≤0%: {norm.cdf(0, loc=np.mean(retornos), scale=np.std(retornos)):.2%}")

# Visualização moderna (substitui o distplot obsoleto)
plt.figure(figsize=(10,6))
sns.histplot(data=retornos, kde=True, bins=50, stat='density')
plt.title('Distribuição de Retornos Diários', fontsize=14)
plt.xlabel('Retorno (%)')
plt.ylabel('Densidade')
plt.grid(True, alpha=0.3)
plt.show()
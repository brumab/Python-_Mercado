# %% [markdown]
# # CAPÍTULO 12 - Google Trends
# ## 12.4 Correlação Preço x Buscas
#!pip install pytrends --quiet
from pytrends.request import TrendReq
import pandas as pd

# Configurar conexão
pytrends = TrendReq(hl='pt-BR', tz=360)

# Buscar termos
pytrends.build_payload(['PETR4', 'ações bolsa'], timeframe='today 12-m')
dados_trends = pytrends.interest_over_time()

# Correlação
correlacao = dados_trends.corr()
print(f"Correlação: {correlacao.iloc[0,1]:.2f}")
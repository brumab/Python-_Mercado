# %% [markdown]
# # CAPÍTULO 13 - IA no Mercado
# ## 13.2 Lógica Fuzzy
#!pip install scikit-fuzzy --quiet
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variáveis fuzzy
volatilidade = ctrl.Antecedent(np.arange(0, 101, 1), 'volatilidade')
recomendacao = ctrl.Consequent(np.arange(0, 101, 1), 'recomendacao')

# Funções de pertinência para volatilidade
volatilidade['baixa'] = fuzz.trimf(volatilidade.universe, [0, 0, 30])
volatilidade['media'] = fuzz.trimf(volatilidade.universe, [20, 50, 80])
volatilidade['alta'] = fuzz.trimf(volatilidade.universe, [70, 100, 100])

# Funções de pertinência para recomendação
recomendacao['compra'] = fuzz.trimf(recomendacao.universe, [60, 80, 100])
recomendacao['neutra'] = fuzz.trimf(recomendacao.universe, [30, 50, 70])
recomendacao['venda'] = fuzz.trimf(recomendacao.universe, [0, 20, 40])

# Regras fuzzy
regra1 = ctrl.Rule(volatilidade['baixa'], recomendacao['compra'])
regra2 = ctrl.Rule(volatilidade['media'], recomendacao['neutra'])
regra3 = ctrl.Rule(volatilidade['alta'], recomendacao['venda'])

# Sistema de controle
sistema = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(sistema)

# Teste com volatilidade de 65
simulador.input['volatilidade'] = 65
simulador.compute()

print(f"Recomendação: {simulador.output['recomendacao']:.0f}/100")


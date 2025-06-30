# %% [markdown]
# # Capítulo 2 - Iteração e Decisão
# ## 2.3 Lógica Condicional
preco = 50.30
if preco > 50:
    print("Acima do target")
elif 49 <= preco <= 50:
    print("Zona neutra")
else:
    print("Abaixo do suporte")

# %% [markdown]
# ## 2.6 For com Range
for i in range(5, 0, -1):  # Contagem regressiva
    print(f"Calculando... {i}")
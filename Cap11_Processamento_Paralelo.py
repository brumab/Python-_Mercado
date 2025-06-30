from multiprocessing import Pool
import time
import numpy as np  # Importação do NumPy para geração de números aleatórios

def simular_montecarlo(ticker):
    # Simulação fictícia de VaR usando distribuição aleatória
    time.sleep(0.5)  # Simulando processamento pesado
    var = np.random.uniform(2, 5)  # Gera um valor aleatório entre 2% e 5%
    return f"{ticker}: VaR 95% = {var:.2f}%"

if __name__ == '__main__':
    # Lista de ativos
    tickers = ['PETR4', 'VALE3', 'BBDC4', 'ITUB4', 'BBAS3']
    
    # Cria um pool de 4 processos paralelos
    with Pool(processes=4) as pool:
        # Executa a simulação em paralelo para cada ticker
        resultados = pool.map(simular_montecarlo, tickers)
    
    # Exibe os resultados
    for res in resultados:
        print(res)

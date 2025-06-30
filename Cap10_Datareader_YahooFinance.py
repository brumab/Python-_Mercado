# -*- coding: utf-8 -*-
"""
Versão corrigida com importação do matplotlib.pyplot
"""
import yfinance as yf
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt  # Importação adicionada aqui
from datetime import datetime

# Configurações
TICKER = 'PETR4.SA'
DATA_INICIO = '2023-01-01'
DATA_FIM = datetime.now().strftime('%Y-%m-%d')

def ajustar_dataframe(df):
    """Remove multi-index e padroniza nomes de colunas"""
    if isinstance(df.columns, pd.MultiIndex):
        df = df.droplevel(0, axis=1)
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    return df

def baixar_dados(ticker):
    """Baixa e ajusta os dados"""
    dados = yf.download(
        ticker,
        start=DATA_INICIO,
        end=DATA_FIM,
        auto_adjust=True,
        progress=False
    )
    return ajustar_dataframe(dados)

def calcular_indicadores(df):
    """Calcula indicadores técnicos"""
    df = df.copy()
    df['MM7'] = df['Close'].rolling(7).mean()
    df['MM21'] = df['Close'].rolling(21).mean()
    return df.dropna()

def plotar_grafico(df):
    """Gera gráfico candlestick"""
    fig, axes = mpf.plot(
        df,
        type='candle',
        style='charles',
        title=f'{TICKER} | {DATA_INICIO} a {DATA_FIM}',
        ylabel='Preço (R$)',
        volume=True,
        mav=(7, 21),
        figratio=(12, 6),
        returnfig=True  # Adicionado para permitir customização
    )
    plt.tight_layout()  # Agora funciona pois plt foi importado
    plt.savefig(f'{TICKER}_chart.png')
    return fig

if __name__ == "__main__":
    try:
        print(f"\nBaixando dados para {TICKER}...")
        dados = baixar_dados(TICKER)
        
        print("\nCalculando indicadores...")
        dados = calcular_indicadores(dados)
        
        print("\nGerando gráfico...")
        figura = plotar_grafico(dados)
        print(f"Gráfico salvo como '{TICKER}_chart.png'")
        plt.show()  # Mostra o gráfico
        
    except Exception as e:
        print(f"\nErro: {str(e)}")
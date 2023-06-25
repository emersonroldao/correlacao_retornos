import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

ativos = ['^BVSP', 'VALE3.SA', 'ITUB4.SA', 'PETR4.SA', 'PETR3.SA', 'ABEV3.SA', 'B3SA3.SA', 'BBAS3.SA', 'BBDC4.SA', 'ELET3.SA', 'ITSA4.SA']

df = yf.download(ativos, start='2023-01-01', end='2023-05-31')['Close']

df.rename(columns={'^BVSP':'IBOV', 'VALE3.SA':'VALE3', 'ITUB4.SA':'ITUB4', 'PETR4.SA':'PETR4', 'PETR3.SA':'PETR3', 'ABEV3.SA':'ABEV3', 'B3SA3.SA':'B3SA3', 'BBAS3.SA':'BBAS3', 'BBDC4.SA':'BBDC4', 'ELET3.SA':'ELET3', 'ITSA4.SA':'ITSA4'}, inplace=True)

retorno = df.pct_change()

retorno.dropna(inplace=True)

plt.figure(figsize=(9, 9))

sns.heatmap(retorno.corr(), vmin = -1, vmax = 1, annot = True, cmap = 'BuPu')

plt.show()

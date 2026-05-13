import statsmodels.tsa.seasonal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

files = os.listdir('../data')
for i in (0, -2):
    series = []
    if '.zip' in files[i]: continue
    print(files[i])
    current = pd.read_csv(f'../data/{files[i]}', names=["xAxis", "yAxis", "BearTemp", "AtmosTemp"])
    series.extend(current['BearTemp'].dropna().values)

    series = pd.Series(series)
    # Декомпозиция
    decomp = statsmodels.tsa.seasonal.seasonal_decompose(series,
                                model='additive',
                                period=25600    )

    # ================== ВИЗУАЛИЗАЦИЯ ==================
    fig = decomp.plot()
    fig.set_size_inches(12, 8)
    plt.suptitle('Seasonal Decomposition - BearTemp', fontsize=14)
    plt.tight_layout()
    plt.show()

    # ================== SNR ==================
    residual = decomp.resid.dropna()
    signal = decomp.trend.dropna() + decomp.seasonal.dropna()

    snr = 10 * np.log10(signal.var() / residual.var())
    print(f"SNR = {snr:.2f} dB")

    # ================== Гистограмма шума ==================
    plt.figure(figsize=(8, 5))
    plt.hist(residual, bins=50, color='skyblue', edgecolor='black')
    plt.title('Распределение остатков (шума)')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.grid(True, alpha=0.3)
    plt.show()
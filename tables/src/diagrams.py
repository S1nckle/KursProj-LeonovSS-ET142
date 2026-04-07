import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from scipy import stats

os.makedirs("../run/diagrams", exist_ok=True)

df = pd.read_csv("../data/StudentPerformanceFactors.csv")

for i, col in enumerate(df.columns):
    plt.figure(figsize=(15, 15))

    if pd.api.types.is_numeric_dtype(df[col]):
        data = df[col].dropna()
        plt.hist(data, bins=30, density=True, alpha=0.7)

        if len(data) > 1:
            kde = stats.gaussian_kde(data)
            x_range = np.linspace(data.min(), data.max(), 100)
            plt.plot(x_range, kde(x_range), 'r-', linewidth=2, label='Плотность')
            plt.legend(fontsize=12)
    else:
        counts = df[col].value_counts()
        counts.plot(kind='bar')

    plt.title(col, fontsize=100)
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)
    plt.tight_layout()
    plt.savefig(f"../run/diagrams/Figure_{i + 1}.png")
    plt.close()
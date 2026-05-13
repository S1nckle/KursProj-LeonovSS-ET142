import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#
files = os.listdir('../data/')

pairs = [
    ('xAxis', 'BearTemp'),
    ('xAxis', 'AtmosTemp'),
    ('yAxis', 'BearTemp'),
    ('yAxis', 'AtmosTemp'),
    ('BearTemp', 'AtmosTemp')
]

results = []

for i in range(0, len(files) - 1) :
    df = pd.read_csv(f"../data/{files[i]}", names=["xAxis", "yAxis", "BearTemp", "AtmosTemp"])
    corr = df.corr()

    row = {'file': files[i].split('/')[-1]}
    for a, b in pairs:
        row[f"{a}_vs_{b}"] = corr.loc[a, b]
    results.append(row)

# Сводная таблица в памяти
summary = pd.DataFrame(results)

print("Средние корреляции по всем файлам:")
print(summary.mean(numeric_only=True).round(4))

# # ================== ГРАФИКИ ==================
numeric_cols = summary.select_dtypes(include='number').columns

plt.figure(figsize=(12, 8))

for i, col in enumerate(numeric_cols, 1):
    plt.subplot(3, 2, i)
    plt.plot(summary[col], color='blue', linewidth=1.2, marker='.', markersize=2)

    mean_val = summary[col].mean()
    plt.axhline(mean_val, color='red', linestyle='--', linewidth=2,
                label=f'Среднее = {mean_val:.4f}')

    plt.title(col.replace('_vs_', ' ↔ '))
    plt.xlabel('Номер файла')
    plt.ylabel('Корреляция')
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# for i in (0, -2):
#     df = pd.read_csv(f"../data/{files[i]}", names=["xAxis", "yAxis", "BearTemp", "AtmosTemp"])
#     print(files[i])
#     corr = df.corr(numeric_only=True)
#
#     plt.figure(figsize=(6, 5))
#     sns.heatmap(corr, annot=True, cmap='YlGnBu', linewidths=.5)
#     plt.tight_layout()
#     plt.show()
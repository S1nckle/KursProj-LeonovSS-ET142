import pandas as pd
import os
import matplotlib.pyplot as plt


def detect_throws_by_3sigma(df):
    throws_count = {}

    for col in df.columns:
        mean_value = df[col].mean()
        std_deviation = df[col].std()

        lower_bound = mean_value - 3 * std_deviation
        upper_bound = mean_value + 3 * std_deviation

        throws = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()

        throws_count[col] = throws

    return throws_count

files = os.listdir("../data")
files = (files[1], files[65], files[128])
for file in files:
    df = pd.read_csv(f'../data/{file}', names=["xAxis", "yAxis", "BearTemp", "AtmosTemp"])
    print(file, ':', sep='')
    print('NA percentage')
    total = len(df)
    missing = df.isna().sum()
    print(missing / total * 100)
    print()
    print('Throws')
    clean_df = df.dropna()
    throws = detect_throws_by_3sigma(clean_df)
    print(throws)

    plt.figure(figsize=(12, 6))
    plt.boxplot(df)
    plt.title(f"Диаграмма размаха для файла {file}")
    plt.xlabel('Значения')
    plt.ylabel('Канал')
    plt.show()

    print('=' * 50)

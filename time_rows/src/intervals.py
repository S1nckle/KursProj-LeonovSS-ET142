import pandas as pd
import matplotlib.pyplot as plt
import os

# Список файлов для анализа
files = os.listdir("../data")
files = (files[1], files[65], files[128])  # индексы файлов

# Цикл по каждому файлу
for file in files:
    # Чтение данных
    df = pd.read_csv(f'../data/{file}', names=["xAxis", "yAxis", "BearTemp", "AtmosTemp"])

    # Преобразование типов данных и очистка пропущенных значений
    df = df.apply(pd.to_numeric, errors='coerce').dropna()

    # Создание нового рисунка
    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))  # два графика вертикально

    # Первый график: механические каналы (xAxis, yAxis)
    axs[0].boxplot([df['xAxis'], df['yAxis']], vert=False)
    axs[0].set_title(f"{file}: Диаграмма размаха для механических каналов")
    axs[0].grid(True, axis='x', linestyle='--', alpha=0.7)
    axs[0].set_yticklabels(['xAxis', 'yAxis'])

    # Второй график: температурные каналы (BearTemp, AtmosTemp)
    axs[1].boxplot([df['BearTemp'], df['AtmosTemp']], vert=False)
    axs[1].set_title(f"{file}: Диаграмма размаха для температурных каналов")
    axs[1].grid(True, axis='x', linestyle='--', alpha=0.7)
    axs[1].set_yticklabels(['BearTemp', 'AtmosTemp'])

    # Общий заголовок для всей фигуры
    fig.suptitle(f"ДИАГРАММЫ РАЗМАХА ПО ФАЙЛУ: {file}", fontsize=14, fontweight='bold')

    # Отображение графика
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    os.makedirs("../run/intervals", exist_ok=True)
    plt.savefig(f"../run/intervals/{file[:-4]}")
    plt.show()
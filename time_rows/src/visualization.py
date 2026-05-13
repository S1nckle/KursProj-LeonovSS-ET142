import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../data/LogFile_2022-06-20-17-00-31.csv", names=["xAxis", "yAxis", "BearTemp", "AtmosTemp"])
fig, axs = plt.subplots(2, 2, figsize=(16, 4))
fig.tight_layout(w_pad=10)
fig.tight_layout(h_pad=3)

axs[0, 0].plot(df["xAxis"], label="xAxis", color="blue")
axs[0, 0].set_title("Вибрация по оси X")
axs[0, 0].set_xlabel("Запись")
axs[0, 0].set_ylabel("Вибрация")
axs[0, 0].grid(True)
axs[0, 0].legend()

axs[0, 1].plot(df["yAxis"], label="yAxis", color="blue")
axs[0, 1].set_title("Вибрация по оси Y")
axs[0, 1].set_xlabel("Запись")
axs[0, 1].set_ylabel("Вибрация")
axs[0, 1].grid(True)
axs[0, 1].legend()

axs[1, 0].plot(df["BearTemp"], label="Температура", color="orange")
axs[1, 0].set_title("Температура подшипника")
axs[1, 0].set_xlabel("Запись")
axs[1, 0].set_ylabel("t°C")
axs[1, 0].grid(True)
axs[1, 0].legend()

axs[1, 1].plot(df["AtmosTemp"], label="Температура", color="orange")
axs[1, 1].set_title("Температура воздуха")
axs[1, 1].set_xlabel("Запись")
axs[1, 1].set_ylabel("t°C")
axs[1, 1].grid(True)
axs[1, 1].legend()

os.makedirs("../run/", exist_ok=True)
plt.savefig("../run/")
plt.show()
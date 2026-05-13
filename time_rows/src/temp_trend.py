import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("..\\data\\LogFile_2022-06-26-01-00-31.csv", names=["AxisX", "AxisY", "TempBearing", "TempAtmos"])
print(len(df))
print(df[0:100])
fig, axs = plt.subplots(1, 4)
# axs[0].plot(df["AxisX"])
# axs[1].plot(df["AxisY"])
axs[2].plot(df["TempBearing"])
axs[3].plot(df["TempAtmos"])
plt.show()

df = pd.read_csv("..\\data\\LogFile_2022-06-20-17-00-31.csv", names=["AxisX", "AxisY", "TempBearing", "TempAtmos"])
print(len(df))
fig, axs = plt.subplots(1, 4)
# axs[0].plot(df["AxisX"])
# axs[1].plot(df["AxisY"])
axs[2].plot(df["TempBearing"])
axs[3].plot(df["TempAtmos"])
plt.show()

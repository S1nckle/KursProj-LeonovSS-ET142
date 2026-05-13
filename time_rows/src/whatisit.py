import pandas as pd

df = pd.read_csv("../data/LogFile_2022-06-26-01-00-31.csv", names=["xAxis", "yAxis", "BearTemp", "AtmosTemp"])

print(df.head())
import pandas as pd

df = pd.read_csv("../data/StudentPerformanceFactors.csv")

l = len(df)
df.drop_duplicates()
print(l - len(df))
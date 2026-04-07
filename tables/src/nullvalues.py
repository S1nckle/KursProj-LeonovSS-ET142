import pandas as pd

df = pd.read_csv("../data/StudentPerformanceFactors.csv")
d = {}

print(df.isnull().sum())
df['Teacher_Quality'] = df['Teacher_Quality'].fillna(df['Teacher_Quality'].mode()[0])
df['Parental_Education_Level'] = df['Parental_Education_Level'].fillna(df['Parental_Education_Level'].mode()[0])
df['Distance_from_Home'] = df['Distance_from_Home'].fillna(df['Distance_from_Home'].mode()[0])
print(df.isnull().sum())


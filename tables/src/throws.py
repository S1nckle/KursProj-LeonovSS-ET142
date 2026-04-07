import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("../data/StudentPerformanceFactors.csv")
df['Teacher_Quality'] = df['Teacher_Quality'].fillna(df['Teacher_Quality'].mode()[0])
df['Parental_Education_Level'] = df['Parental_Education_Level'].fillna(df['Parental_Education_Level'].mode()[0])
df['Distance_from_Home'] = df['Distance_from_Home'].fillna(df['Distance_from_Home'].mode()[0])

mapping = {
    'Low': 0, 'Medium': 1, 'High': 2,
    'Yes': 1, 'No': 0,
    'Positive': 1, 'Negative': -1, 'Neutral': 0,
    'Public': 0, 'Private': 1,
    'High School': 0, 'College': 1, 'Postgraduate': 2,
    'Near': 0, 'Moderate': 1, 'Far': 2,
    'Male': 0, 'Female': 1
}

for col in df.select_dtypes(['string']).columns.to_list():
    df[col] = df[col].map(mapping)


for col in df.head():
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1-1.5*IQR, Q3+1.5*IQR
    pct_outliers = ((df[col] < lower) | (df[col] > upper)).mean()
    print(f"{col}: {pct_outliers:.1%} выбросов")
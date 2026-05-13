import pandas as pd
import os

files = os.listdir("../data")
files = (files[1], files[65], files[128])
for file in files:
    df = pd.read_csv(f'../data/{file}', names=["xAxis", "yAxis", "BearTemp", "AtmosTemp"])
    print(file + ':')
    print(df.describe())
    print(df.median())
    print('IsNA:\n', df.isnull().sum(), sep='')

    print('=' * 100)
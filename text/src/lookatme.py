import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_json('../data/unstable_universe_dataset.jsonl', lines=True)

print(df.head())
print(df['content'][3])
print(len(df))


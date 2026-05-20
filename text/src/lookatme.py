import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_json('../data/unstable_universe_dataset_lemmatized.jsonl', lines=True)

print(df.head())
# print(df['content'][:15])
# print(df['clean_content'][:15])
# print(df['lemmatized'][:15])


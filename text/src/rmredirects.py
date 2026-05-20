import pandas as pd

df = pd.read_json('../data/unstable_universe_dataset.jsonl', lines=True)
n = len(df)
print(f'До очистки: {n} записей.')
df = df[~df['content'].str.contains('redirect', case=False, na=False)].copy()
print(f"После очистки: {len(df)} записей.")
print(f"Удалено {n - len(df)} записей.")

df.to_json('../data/unstable_universe_dataset_no_redirect.jsonl',
           orient='records',
           lines=True,
           force_ascii=False)

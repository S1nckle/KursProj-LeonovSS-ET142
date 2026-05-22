import re
import pandas as pd

df = pd.read_json('../data/unstable_universe_dataset_no_redirect.jsonl', lines=True)


def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    #
    # Оставляем только буквы, цифры и _
    text = re.sub(r'[^a-z0-9_`\' ]', ' ', text)
    text = ' '.join(text.split())
    return text

df['clean_content'] = df['content'].apply(clean_text)

# Покажем, как изменился текст
print(f"До:  {df['content'][3]}")
print(f"После: {df['clean_content'][3]}")

df.to_json('../data/unstable_universe_dataset_clean.jsonl',
           orient='records',
           lines=True,
           force_ascii=False)
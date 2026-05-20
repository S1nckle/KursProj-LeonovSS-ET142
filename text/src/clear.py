import re
import pandas as pd

df = pd.read_json('../data/unstable_universe_dataset_no_redirect.jsonl', lines=True)


def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    #Удаляем ссылки
    text = re.sub(r'https?://\S+|www\.\S+|\b\w+\.(com|org|net|wiki|fandom)\b', ' ', text)
    # Оставляем только буквы, цифры и _
    text = re.sub(r'[^a-z0-9_ ]', ' ', text)

    tokens = text.split()
    cleaned = []

    for token in tokens:
        if len(token) < 2:
            continue

        # Убираем цифры только в начале и в конце
        cleaned_token = re.sub(r'^[0-9]+', '', token)
        cleaned_token = re.sub(r'[0-9]+$', '', cleaned_token)

        if any(c.isalpha() for c in token):
            cleaned.append(token)

    return " ".join(cleaned)

df['clean_content'] = df['content'].apply(clean_text)

# Покажем, как изменился текст
print(f"До:  {df['content'][15]}")
print(f"После: {df['clean_content'][15]}")

df.to_json('../data/unstable_universe_dataset_clean.jsonl',
           orient='records',
           lines=True,
           force_ascii=False)
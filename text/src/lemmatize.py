import spacy
import pandas as pd
# pip install spacy
# python -m spacy download en_core_web_lg
i = 0
nlp = spacy.load("en_core_web_lg")
df = pd.read_json('../data/unstable_universe_dataset_clean.jsonl', lines=True)

def lemmatize_text(text):
    global i
    print(i,end=' ')
    i += 1
    """Простая функция для одного текста"""
    doc = nlp(text)
    return " ".join([token.lemma_ if token.text != 'spoke' else token.text for token in doc ])

df['lemmatized'] = df['clean_content'].apply(lemmatize_text)

print('До: \n', df['clean_content'][15])
print('После: \n', df['lemmatized'][15])

df.to_json('../data/unstable_universe_dataset_lemmatized.jsonl',
           orient='records',
           lines=True,
           force_ascii=False)
import spacy
import pandas as pd

i = 0
# Загружаем модель
nlp = spacy.load("en_core_web_lg")

df = pd.read_json('../data/unstable_universe_dataset_lemmatized.jsonl', lines=True)

def remove_stop_words(text):
    global i
    print(i,end=' ')
    i += 1
    doc = nlp(text)
    return ' '.join([token.text for token in doc if not token.is_stop and len(token.text) > 1])


df['no_stopwords'] = df['lemmatized'].apply(remove_stop_words)
print("До:   ", df['lemmatized'][15])
print("После:", df['no_stopwords'][15])

df.to_json('../data/unstable_universe_dataset_no_stopwords.jsonl',
           orient='records',
           lines=True,
           force_ascii=False)


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import re

from spacy.lang.en import STOP_WORDS


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

nlp = spacy.load("en_core_web_lg")

def lemmatize_text(text):
    doc = nlp(text)
    return " ".join([token.lemma_ if token.text != 'spoke' else token.text for token in doc ])

def remove_stop_words(text):
    doc = nlp(text)
    return ' '.join([token.text for token in doc if not token.is_stop and len(token.text) > 1])


# функция поиска наиболее близких текстов к запросу
def search_texts(query, vectorizer, tfidf_matrix, texts, top_n=3):
    """
    Ищет top_n текстов, наиболее похожих на запрос.
    """
    query = clean_text(query)            # очищаем запрос
    query = lemmatize_text(query)        # лемматизируем запрос
    query_vec = vectorizer.transform([query])  # векторизуем запрос

    # считаем похожесть запроса со всеми текстами
    similarities = cosine_similarity(query_vec, tfidf_matrix)[0]

    # находим индексы топ-n самых похожих
    top_indices = similarities.argsort()[-top_n:][::-1]

    results = []
    for idx in top_indices:
        results.append({
            'Текст': texts.iloc[idx],
            'Похожесть': similarities[idx]
        })

    return results

df = pd.read_json('../data/unstable_universe_dataset_no_stopwords.jsonl', lines=True)

# создаём и обучаем векторайзер
vectorizer = TfidfVectorizer(stop_words=list(STOP_WORDS))  # обычно именно тут удаляют стоп-слова, а не ранее, как это сделали мы
tfidf_matrix = vectorizer.fit_transform(df['no_stopwords'])

# Пример поиска
query = "spoke and jamatop"
results = search_texts(query, vectorizer, tfidf_matrix, df['no_stopwords'], top_n=5)

print(f"Поисковый запрос: '{query}'")
print(f"\nНайдено {len(results)} наиболее похожих текстов:\n")
for i, res in enumerate(results, 1):
    print(f"{i}. Похожесть: {res['Похожесть']:.8f}")
    print(f"   Текст: {res['Текст']}")
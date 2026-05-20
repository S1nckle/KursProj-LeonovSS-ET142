from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from spacy.lang.en import STOP_WORDS
import numpy as np
np.set_printoptions(
    threshold=np.inf,      # показывать все элементы
    linewidth=200,         # ширина строки (чтобы меньше переносилось)
    suppress=True,         # не использовать научную нотацию
    precision=4            # сколько знаков после запятой
)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

df = pd.read_json('../data/unstable_universe_dataset_no_stopwords.jsonl', lines=True)

# создаём и обучаем векторайзер
vectorizer = TfidfVectorizer(stop_words=list(STOP_WORDS))  # обычно именно тут удаляют стоп-слова, а не ранее, как это сделали мы
tfidf_matrix = vectorizer.fit_transform(df['no_stopwords'])

# получаем список всех слов (словарь)
feature_names = vectorizer.get_feature_names_out()
print(f"Размер словаря: {len(feature_names)} слов")

print(f"Текст: {df['no_stopwords'].iloc[100]}")
print(f"Вектор:\n{tfidf_matrix[0].toarray()}")
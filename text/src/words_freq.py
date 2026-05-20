from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('../data/unstable_universe_dataset_lemmatized.jsonl', lines=True)
# Объединяем все леммы в один список слов
all_words = ' '.join(df['lemmatized']).split()

# Считаем частоту каждого слова
word_counts = Counter(all_words)
    
print("Топ-10 самых частых слов:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")


# Берём топ-10 и разделяем на слова и частоты
top_words = word_counts.most_common(10)
words, counts = zip(*top_words)

plt.figure(figsize=(10, 5))
plt.bar(words, counts, color='steelblue')
plt.title('Топ-10 самых частых слов')
plt.xlabel('Слово')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
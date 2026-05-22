from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json('../data/unstable_universe_dataset_lemmatized.jsonl', lines=True)

# Создаём облако слов
all_text = ' '.join(df['lemmatized'])
wc = WordCloud(width=800, height=400, background_color='white').generate(all_text)

# Показываем
plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('Частые слова в статьях wiki')
plt.show()
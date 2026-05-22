import requests
import time
import json
import re
from tqdm import tqdm
from bs4 import BeautifulSoup

WIKI_BASE = "https://unstable-universe-mc.fandom.com"


def get_all_page_titles():
    pages = []
    params = {
        "action": "query",
        "list": "allpages",
        "apnamespace": 0,
        "aplimit": 500,
        "format": "json"
    }
    while True:
        response = requests.get(f"{WIKI_BASE}/api.php", params=params)
        data = response.json()
        pages.extend([p["title"] for p in data["query"]["allpages"]])

        if "continue" not in data:
            break
        params["apcontinue"] = data["continue"]["apcontinue"]
        time.sleep(0.3)  # вежливость

    return pages


def get_clean_text(title):
    """Получаем максимально чистый текст страницы"""
    params = {
        "action": "parse",
        "page": title,
        "prop": "text",  # HTML-версия
        "format": "json",
        "disableeditsection": True,
        "disabletoc": True
    }

    try:
        response = requests.get(f"{WIKI_BASE}/api.php", params=params, timeout=10)
        data = response.json()

        html = data["parse"]["text"]["*"]

        # Парсим HTML и извлекаем чистый текст
        soup = BeautifulSoup(html, "html.parser")

        # Удаляем ненужные элементы
        for unwanted in soup.select("table, .infobox, .navbox, .metadata, .mw-editsection, style, script"):
            unwanted.decompose()

        # Извлекаем текст
        text = soup.get_text(separator="\n")

        text = text.strip()

        return text

    except Exception as e:
        print(f"Ошибка при обработке {title}: {e}")
        return get_clean_text(title)


# ======================
# Запуск
# ======================
print("Получаем список страниц...")
titles = get_all_page_titles()
print(f"Найдено страниц: {len(titles)}")

dataset = []

for title in tqdm(titles):
    clean_text = get_clean_text(title)

    dataset.append({
        "title": title,
        "url": f"{WIKI_BASE}/wiki/{title.replace(' ', '_')}",
        "content": clean_text
    })

    time.sleep(0.5)  # вежливость к серверу

# Сохранение
with open("../data/unstable_universe_dataset_clean2.jsonl", "w", encoding="utf-8") as f:
    for item in dataset:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"\nГотово! Сохранено {len(dataset)} статей.")
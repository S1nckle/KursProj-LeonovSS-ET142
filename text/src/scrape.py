import requests
import time
import json
from tqdm import tqdm
import mwparserfromhell

WIKI = "https://unstable-universe-mc.fandom.com"


def get_all_pages():
    pages = []
    params = {
        "action": "query",
        "list": "allpages",
        "apnamespace": 0,
        "aplimit": 500,
        "format": "json"
    }
    while True:
        response = requests.get(f"{WIKI}/api.php", params=params)
        data = response.json()
        pages.extend([p["title"] for p in data["query"]["allpages"]])

        if "continue" not in data:
            break
        params["apcontinue"] = data["continue"]["apcontinue"]
        time.sleep(0.3)  # вежливость

    return pages


def get_page_content(title):
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "titles": title,
        "format": "json"
    }
    response = requests.get(f"{WIKI}/api.php", params=params)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    wikitext = page["revisions"][0]["*"] if "revisions" in page else ""
    return wikitext


# ======================
# Основной запуск
# ======================
pages = get_all_pages()
print(f"Найдено страниц: {len(pages)}")

dataset = []

for title in tqdm(pages):
    wikitext = get_page_content(title)
    # Очистка
    parsed = mwparserfromhell.parse(wikitext)
    clean_text = parsed.strip_code()  # убирает большую часть вики-разметки

    dataset.append({
        "title": title,
        "url": f"{WIKI}/wiki/{title.replace(' ', '_')}",
        "content": clean_text,
        "raw_wikitext": wikitext  # на всякий случай
    })
    time.sleep(0.3)  # чтобы не попасть под rate-limit

# Сохранение
with open("../data/unstable_universe_dataset.jsonl", "w", encoding="utf-8") as f:
    for item in dataset:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
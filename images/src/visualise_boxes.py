import cv2
import pandas as pd
from pathlib import Path

# ================= НАСТРОЙКИ =================
csv_path = '../data/bounding_boxes/train_labels.csv'  # путь к твоему CSV
images_dir = Path('../data/images/train')  # папка с оригинальными изображениями
output_dir = Path('../run/')  # папка, куда будут сохраняться изображения с боксами

# Цвет и толщина бокса
BOX_COLOR = (0, 255, 0)  # зелёный (BGR)
BOX_THICKNESS = 3
TEXT_COLOR = (0, 255, 0)
FONT_SCALE = 0.8
# ============================================

df = pd.read_csv(csv_path)

# Создаём папку для сохранения, если её нет
output_dir.mkdir(exist_ok=True)

print(f"Найдено {df['filename'].nunique()} уникальных изображений и {len(df)} боксов.")
print(f"Изображения будут сохранены в папку: {output_dir}\n")

processed = 0
missing = 0

for filename, group in df.groupby('filename'):
    img_path = images_dir / filename

    if not img_path.exists():
        print(f"⚠️  Изображение не найдено: {filename}")
        missing += 1
        continue

    img = cv2.imread(str(img_path))
    if img is None:
        print(f"⚠️  Не удалось загрузить: {filename}")
        missing += 1
        continue

    # Рисуем все bounding boxes для этого изображения
    for _, row in group.iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])

        # Рисуем прямоугольник
        cv2.rectangle(img, (x1, y1), (x2, y2), BOX_COLOR, BOX_THICKNESS)

        # Подписываем класс (Graffiti)
        label = row['class']
        cv2.putText(img, label, (x1, max(y1 - 10, 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, FONT_SCALE, TEXT_COLOR, 2)

    # Сохраняем изображение
    save_path = output_dir / filename
    cv2.imwrite(str(save_path), img)

    processed += 1
    if processed % 50 == 0:
        print(f"✓ Обработано: {processed} изображений")

print("\nГотово!")
print(f"Успешно сохранено: {processed} изображений")
if missing > 0:
    print(f"Пропущено (не найдено): {missing} изображений")
print(f"\nПапка с результатами: {output_dir.resolve()}")
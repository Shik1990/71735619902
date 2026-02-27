# mood_diary/core.py
"""
Основные функции дневника настроений.

Важно: Нет импорта config.py!
Путь к файлу данных передаётся как параметр (Dependency Injection).
"""

from pathlib import Path
from datetime import datetime
from .validators import validate_mood


def add_entry(mood: str, data_file: Path) -> bool:
    """
    Добавляет запись в дневник.

    Аргументы:
        mood: Настроение пользователя
        data_file: Путь к файлу данных (передаётся из main.py)

    Возвращает:
        True если успешно, False иначе

    Преимущества:
        ✅ Нет зависимости от config.py
        ✅ Легко тестировать (передаём тестовый путь)
        ✅ Явная зависимость (видно по параметрам)
    """
    try:
        mood_valid = validate_mood(mood)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {mood_valid}\n"

        # Создаём папку если нет
        data_file.parent.mkdir(parents=True, exist_ok=True)

        # Записываем в файл
        with data_file.open('a', encoding='utf-8') as f:
            f.write(entry)

        print(f"✅ Запись добавлена: {entry.strip()}")
        return True

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False


def get_all_entries(data_file: Path) -> list:
    """
    Возвращает все записи из дневника.

    Аргументы:
        data_file: Путь к файлу данных

    Возвращает:
        Список строк с записями (пустой список если файл не существует)
    """
    if not data_file.exists():
        return []

    with data_file.open('r', encoding='utf-8') as f:
        return f.read().splitlines()


def get_mood_stats(data_file: Path) -> dict:
    """
    Возвращает статистику по настроениям.

    Аргументы:
        data_file: Путь к файлу данных

    Возвращает:
        Словарь {настроение: количество}
    """
    entries = get_all_entries(data_file)
    stats = {}

    for entry in entries:
        if ']' in entry:
            mood = entry.split(']')[-1].strip()
            stats[mood] = stats.get(mood, 0) + 1

    return stats


def show_stats(data_file: Path) -> None:
    """
    Показывает статистику по настроениям.

    Аргументы:
        data_file: Путь к файлу данных
    """
    stats = get_mood_stats(data_file)

    if not stats:
        print("📭 Нет записей")
        return

    print("\n📊 Статистика настроений:")
    for mood, count in stats.items():
        print(f"  {mood}: {count}")
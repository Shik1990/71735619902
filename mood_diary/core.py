# mood_diary/core.py
"""Основные функции дневника настроений"""

import sys
from pathlib import Path
from datetime import datetime

# Добавляем корень проекта в sys.path для импорта config
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import DATA_FILE
from .validators import validate_mood


def add_entry(mood: str) -> bool:
    """Добавляет запись в дневник."""
    try:
        mood_valid = validate_mood(mood)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {mood_valid}\n"

        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with DATA_FILE.open('a', encoding='utf-8') as f:
            f.write(entry)

        print(f"✅ Запись добавлена: {entry.strip()}")
        return True

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False


def get_all_entries() -> list:
    """Возвращает все записи из дневника."""
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open('r', encoding='utf-8') as f:
        return f.read().splitlines()


def get_mood_stats() -> dict:
    """Возвращает статистику по настроениям."""
    entries = get_all_entries()
    stats = {}

    for entry in entries:
        if ']' in entry:
            mood = entry.split(']')[-1].strip()
            stats[mood] = stats.get(mood, 0) + 1

    return stats


def show_stats():
    """Показывает статистику."""
    stats = get_mood_stats()

    if not stats:
        print("📭 Нет записей")
        return

    print("\n📊 Статистика настроений:")
    for mood, count in stats.items():
        print(f"  {mood}: {count}")
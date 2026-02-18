from pathlib import Path
from datetime import datetime
from .config import MOOD_FILE, DATE_FORMAT, ENCODING

#MOOD_FILE = Path("data/entries.txt")


def add_entry(mood: str) -> bool:
    """Добавляет запись в дневник."""
    try:

        timestamp = datetime.now().strftime(DATE_FORMAT)
        entry = f"[{timestamp}] {mood}\n"

        MOOD_FILE.parent.mkdir(parents=True, exist_ok=True)

        with MOOD_FILE.open('a', encoding=ENCODING) as f:
            f.write(entry)

        print(f"✅ Запись добавлена: {entry.strip()}")
        return True

    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False


def get_all_entries() -> list:
    """Возвращает все записи из дневника."""
    if not MOOD_FILE.exists():
        return []

    return MOOD_FILE.read_text(encoding=ENCODING).splitlines()
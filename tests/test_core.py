# tests/test_core.py
"""
Тесты для модуля core.

Запуск:
    python tests/test_core.py
    или
    pytest tests/test_core.py
"""

import sys
from pathlib import Path

# Добавляем корень проекта в sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from mood_diary.core import add_entry, get_all_entries, get_mood_stats


def test_add_entry():
    """Тест добавления записи"""
    # Создаём временный тестовый файл
    test_file = Path("/tmp/test_mood.txt")

    # Очищаем если есть
    if test_file.exists():
        test_file.unlink()

    # Тест добавления
    result = add_entry("good", test_file)
    assert result == True, "Должно вернуть True"

    # Тест чтения
    entries = get_all_entries(test_file)
    assert len(entries) == 1, f"Ожидал 1 запись, получил {len(entries)}"
    assert "good" in entries[0], "Запись должна содержать 'good'"

    # Очищаем
    test_file.unlink()

    print("✅ test_add_entry")


def test_get_mood_stats():
    """Тест статистики настроений"""
    # Создаём временный файл с данными
    test_file = Path("/tmp/test_stats.txt")
    test_file.write_text("[2026-02-12 15:30:45] good\n[2026-02-12 15:31:00] bad\n")

    # Тест статистики
    stats = get_mood_stats(test_file)
    assert stats.get("good") == 1
    assert stats.get("bad") == 1

    # Очищаем
    test_file.unlink()

    print("✅ test_get_mood_stats")


if __name__ == "__main__":
    test_add_entry()
    test_get_mood_stats()
    print("\n🎉 Все тесты прошли!")
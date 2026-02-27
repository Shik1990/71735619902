# tests/test_validators.py
"""
Тесты для модуля validators.

Запуск:
    python tests/test_validators.py
    или
    pytest tests/test_validators.py
"""

import sys
from pathlib import Path

# Добавляем корень проекта в sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from mood_diary.validators import validate_mood, is_valid_mood, VALID_MOODS


def test_is_valid_mood():
    """Тест проверки валидности настроения"""
    assert is_valid_mood("good") == True
    assert is_valid_mood("GOOD") == True  # Регистронезависимо
    assert is_valid_mood("  bad  ") == True  # Пробелы игнорируются
    assert is_valid_mood("neutral") == True
    assert is_valid_mood("excellent") == True
    assert is_valid_mood("fantastic") == False
    assert is_valid_mood("") == False
    print("✅ test_is_valid_mood")


def test_validate_mood():
    """Тест валидации настроения"""
    assert validate_mood("GOOD") == "good"
    assert validate_mood("  Bad  ") == "bad"
    assert validate_mood("neutral") == "neutral"
    assert validate_mood("excellent") == "excellent"

    # Тест на ошибку
    try:
        validate_mood("invalid")
        assert False, "Должно было выбросить ValueError"
    except ValueError as e:
        assert "Некорректное настроение" in str(e)

    print("✅ test_validate_mood")


def test_valid_moods_constant():
    """Тест константы VALID_MOODS"""
    assert isinstance(VALID_MOODS, tuple)
    assert len(VALID_MOODS) > 0
    assert "good" in VALID_MOODS
    assert "bad" in VALID_MOODS
    print("✅ test_valid_moods_constant")


if __name__ == "__main__":
    test_is_valid_mood()
    test_validate_mood()
    test_valid_moods_constant()
    print("\n🎉 Все тесты прошли!")
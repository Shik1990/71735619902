# mood_diary/validators.py
"""Функции валидации для дневника настроений"""

# Константы предметной области (НЕ в config.py!)
VALID_MOODS = ('good', 'bad', 'neutral', 'excellent')


def is_valid_mood(mood: str) -> bool:
    """
    Проверяет, является ли настроение допустимым.

    Аргументы:
        mood: Строка с настроением

    Возвращает:
        True если валидно, False иначе
    """
    return mood.strip().lower() in VALID_MOODS


def validate_mood(mood: str) -> str:
    """
    Валидирует настроение и возвращает нормализованное значение.

    Аргументы:
        mood: Строка с настроением

    Возвращает:
        Нормализованное настроение (lowercase, без пробелов)

    Исключения:
        ValueError: Если настроение не в списке допустимых
    """
    mood_clean = mood.strip().lower()

    if mood_clean not in VALID_MOODS:
        valid_str = "', '".join(VALID_MOODS)
        raise ValueError(
            f"Некорректное настроение: '{mood}'. "
            f"Допустимые значения: '{valid_str}'"
        )

    return mood_clean


def get_mood_from_input() -> str:
    """
    Запрашивает настроение у пользователя через input().

    Возвращает:
        Валидное настроение от пользователя
    """
    while True:
        user_input = input(f"Введите настроение {VALID_MOODS}: ")

        try:
            return validate_mood(user_input)
        except ValueError as e:
            print(f"❌ {e}\n")
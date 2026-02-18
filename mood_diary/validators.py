from .config import VALID_MOODS
#VALID_MOODS = ('good', 'bad', 'neutral', 'excellent')

def validate_mood() -> str:
    """Валидирует настроение."""
    while True:
        mood_clean = input(f"Введите настроение из списка: {VALID_MOODS}").strip().lower()
        try:
            if mood_clean not in VALID_MOODS:
                valid_str = "', '".join(VALID_MOODS)
                raise ValueError(f"Некорректное настроение: '{mood_clean}'. Допустимые: '{valid_str}'")
            return mood_clean
        except ValueError as e:
            print(f"Ошибка! {e}")


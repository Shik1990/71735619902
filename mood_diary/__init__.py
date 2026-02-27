# mood_diary/__init__.py
"""
Пакет для работы с дневником настроений.

Пример использования:
    from mood_diary import add_entry, show_stats
    add_entry("good", data_file)
    show_stats(data_file)
"""

__version__ = "0.1.0"

# Импортируем функции из модулей пакета
from .core import add_entry, get_all_entries, get_mood_stats, show_stats
from .validators import validate_mood, is_valid_mood, get_mood_from_input

# Публичный API — что доступно при импорте
__all__ = [
    'add_entry',
    'get_all_entries',
    'get_mood_stats',
    'show_stats',
    'validate_mood',
    'is_valid_mood',
    'get_mood_from_input',
]
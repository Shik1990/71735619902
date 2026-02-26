# mood_diary/__init__.py
"""Пакет для работы с дневником настроений"""

__version__ = "0.1.0"

# Импортируем функции пакета
from .core import add_entry, get_all_entries, get_mood_stats
from .validators import validate_mood, is_valid_mood
from .config import APP_NAME, DEBUG, get_data_file, is_debug
# Публичный API
__all__ = [
    'add_entry',
    'get_all_entries',
    'get_mood_stats',
    'validate_mood',
    'is_valid_mood',
]
# mood_diary/__init__.py
"""Пакет для работы с дневником настроений"""

__version__ = "0.1.0"

import sys

# Импортируем функции пакета
from .core import add_entry, get_all_entries, get_mood_stats, show_stats
from .validators import validate_mood, is_valid_mood

# Публичный API
__all__ = [
    'add_entry',
    'get_all_entries',
    'get_mood_stats',
    'show_stats',
    'validate_mood',
    'is_valid_mood',
    ]

print(sys.path)
"""Пакет для работы с дневником настроений"""
__all__ = [
    "add_entry",
    "get_all_entries",
    "validate_mood"
]

from .core import add_entry, get_all_entries
from .validators import validate_mood

__version__ = "0.1.0"
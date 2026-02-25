"""
from pathlib import Path


# Все настройки в одном месте!
MOOD_FILE_PATH = "data/entries.txt"
BASE_DIR = Path(__file__).parent.parent
MOOD_FILE = BASE_DIR / MOOD_FILE_PATH
VALID_MOODS = ('good', 'bad', 'neutral', 'excellent')

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
ENCODING = "utf-8"
MAX_ENTRIES = 1000
"""

# config.py
"""
Модуль конфигурации проекта.
Загружает переменные окружения из файла .env
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# === Шаг 1: Загружаем .env файл ===
# Находим папку где лежит этот файл
BASE_DIR = Path(__file__).parent

# Путь к файлу .env
ENV_FILE = BASE_DIR / ".env"

# Загружаем переменные из .env в окружение
load_dotenv(ENV_FILE)

# === Шаг 2: Получаем переменные ===

# Простые переменные (строки)
APP_NAME = os.getenv("APP_NAME", "Mood Diary")  # Значение по умолчанию
DEBUG = os.getenv("DEBUG", "False").lower() == "true"  # Преобразуем в bool
VERSION = os.getenv("VERSION", "1.0.0")

# Пути (преобразуем в Path)
DATA_FILE_PATH = Path(os.getenv("DATA_FILE_PATH", "data/entries.txt"))
DATA_FILE = BASE_DIR / DATA_FILE_PATH  # Полный путь

# Секретный ключ (обязательный!)
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY не найден в .env! Проверь файл .env")

# API ключи (опциональные)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# База данных
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "name": os.getenv("DB_NAME", "mood_diary"),
    "user": os.getenv("DB_USER", "userv"),
    "password": os.getenv("DB_PASSWORD", ""),
}

# === Шаг 3: Вспомогательные функции ===

def is_debug() -> bool:
    """Проверка режима отладки"""
    return DEBUG

def get_data_file() -> Path:
    """Получить полный путь к файлу данных"""
    # Создаём папку если нет
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    return DATA_FILE

def get_db_connection_string() -> str:
    """Получить строку подключения к БД"""
    return (
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['name']}"
    )
MOOD_FILE_PATH = "data/entries.txt"
BASE_DIR = Path(__file__).parent.parent
MOOD_FILE = BASE_DIR / MOOD_FILE_PATH
VALID_MOODS = ('good', 'bad', 'neutral', 'excellent')

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
ENCODING = "utf-8"
MAX_ENTRIES = 1000
# === Шаг 4: Проверка конфигурации (для отладки) ===
if __name__ == "__main__":
    print(f"📋 Конфигурация проекта:")
    print(f"  APP_NAME: {APP_NAME}")
    print(f"  DEBUG: {DEBUG}")
    print(f"  VERSION: {VERSION}")
    print(f"  DATA_FILE: {DATA_FILE}")
    print(f"  SECRET_KEY: {'*' * len(SECRET_KEY)}")  # Скрываем ключ
    print(f"  TELEGRAM_BOT_TOKEN: {'✅' if TELEGRAM_BOT_TOKEN else '❌'}")
    print(f"  DB_CONFIG: {DB_CONFIG}")
# config.py
"""
Модуль конфигурации проекта.
Загружает переменные окружения из файла .env

Это ЕДИНСТВЕННОЕ место где определяются пути и настройки!
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# === Шаг 1: Находим путь к .env ===
BASE_DIR = Path(__file__).parent
ENV_FILE = BASE_DIR / ".env"

# === Шаг 2: Загружаем .env ===
load_dotenv(ENV_FILE)

# === Шаг 3: Получаем переменные ===

# Простые строки
APP_NAME = os.getenv("APP_NAME", "Mood Diary")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
VERSION = os.getenv("VERSION", "1.0.0")

# Пути
DATA_FILE_PATH = os.getenv("DATA_FILE_PATH", "data/entries.txt")
DATA_FILE = BASE_DIR / DATA_FILE_PATH

# Секретный ключ (ОБЯЗАТЕЛЬНЫЙ!)
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("⚠️ SECRET_KEY не найден в .env!")

# Опциональные API ключи
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


# === Шаг 4: Вспомогательные функции ===

def is_debug() -> bool:
    """Проверка режима отладки"""
    return DEBUG


def get_data_file() -> Path:
    """
    Получить полный путь к файлу данных.

    Создаёт папку если она не существует.
    """
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    return DATA_FILE


def get_db_connection_string() -> str:
    """Получить строку подключения к БД"""
    return (
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['name']}"
    )


# === Шаг 5: Тест при запуске ===
if __name__ == "__main__":
    print("📋 Конфигурация проекта:")
    print(f"  APP_NAME: {APP_NAME}")
    print(f"  DEBUG: {DEBUG}")
    print(f"  VERSION: {VERSION}")
    print(f"  DATA_FILE: {DATA_FILE}")
    print(f"  SECRET_KEY: {'*' * len(SECRET_KEY)}")
    print(f"  TELEGRAM_BOT_TOKEN: {'✅' if TELEGRAM_BOT_TOKEN else '❌'}")
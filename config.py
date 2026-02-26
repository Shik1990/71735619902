# config.py (в корне проекта!)
"""
Модуль конфигурации проекта.
Загружает переменные окружения из файла .env
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# === Шаг 1: Находим путь к .env ===
BASE_DIR = Path(__file__).parent  # Теперь это корень проекта!
ENV_FILE = BASE_DIR / ".env"

# === Шаг 2: Загружаем .env ===
load_dotenv(ENV_FILE)

# === Шаг 3: Получаем переменные ===
APP_NAME = os.getenv("APP_NAME", "Mood Diary")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
VERSION = os.getenv("VERSION", "1.0.0")

DATA_FILE_PATH = os.getenv("DATA_FILE_PATH", "data/entries.txt")
DATA_FILE = BASE_DIR / DATA_FILE_PATH

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("⚠️ SECRET_KEY не найден в .env!")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# === Шаг 4: Вспомогательные функции ===
def is_debug() -> bool:
    return DEBUG

def get_data_file() -> Path:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    return DATA_FILE

# === Шаг 5: Тест ===
if __name__ == "__main__":
    print("📋 Конфигурация:")
    print(f"  APP_NAME: {APP_NAME}")
    print(f"  DEBUG: {DEBUG}")
    print(f"  VERSION: {VERSION}")
    print(f"  DATA_FILE: {DATA_FILE}")
    print(f"  SECRET_KEY: {'*' * len(SECRET_KEY)}")
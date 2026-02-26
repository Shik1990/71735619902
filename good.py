""""# test_install.py
import sys
print(f"Python: {sys.executable}")
print(f"Путь: {sys.path}")

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv установлен!")
except ImportError:
    print("❌ python-dotenv НЕ установлен")"""
import os
from dotenv import load_dotenv

# Загружаем все переменные из .env
load_dotenv()

# Теперь можно использовать os.getenv()
database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
api_key = os.getenv("API_KEY")
debug = os.getenv("DEBUG")

print(f"Подключаюсь к базе: {database_url}")
print(f"Ключ API: {api_key}")
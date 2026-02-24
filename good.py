# test_install.py
import sys
print(f"Python: {sys.executable}")
print(f"Путь: {sys.path}")

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv установлен!")
except ImportError:
    print("❌ python-dotenv НЕ установлен")
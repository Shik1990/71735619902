# main.py
"""Основная программа дневника настроений"""

from config import APP_NAME, VERSION, get_data_file, is_debug, DEBUG
from mood_diary import add_entry, get_all_entries, show_stats


def main():
    """Главная функция"""

    print(f"🌟 {APP_NAME}")
    print(f"📊 Версия: {VERSION}")
    print("=" * 50)

    if is_debug():
        print("⚠️  Режим отладки включён!")

    data_file = get_data_file()
    print(f"📁 Файл данных: {data_file}")

    while True:
        print("\nМеню:")
        print("1. Добавить запись")
        print("2. Показать статистику")
        print("3. Выход")

        choice = input("\nВыберите действие (1-3): ").strip()

        if choice == '1':
            mood = input("Введите настроение: ")
            add_entry(mood)

        elif choice == '2':
            show_stats()

        elif choice == '3':
            print("👋 До свидания!")
            break

        else:
            print("❌ Некорректный выбор")


if __name__ == "__main__":
    main()
# main.py
"""
Основная программа дневника настроений.

Собирает всё вместе:
1. Получает настройки из config.py
2. Передаёт зависимости в функции mood_diary
3. Управляет основным циклом программы
"""

from config import APP_NAME, DEBUG, VERSION, get_data_file, is_debug
from mood_diary import add_entry, show_stats, get_mood_from_input


def main():
    """Главная функция"""

    # Приветствие
    print(f"🌟 {APP_NAME}")
    print(f"📊 Версия: {VERSION}")
    print("=" * 50)

    if is_debug():
        print("⚠️  Режим отладки включён!")

    # Получаем путь к файлу данных (ЕДИНСТВЕННОЕ место где это происходит)
    data_file = get_data_file()
    print(f"📁 Файл данных: {data_file}")

    # Основной цикл
    while True:
        print("\nМеню:")
        print("1. Добавить запись")
        print("2. Показать статистику")
        print("3. Выход")

        choice = input("\nВыберите действие (1-3): ").strip()

        if choice == '1':
            # Получаем настроение от пользователя
            mood = get_mood_from_input()
            # Передаём путь явно (Dependency Injection)
            add_entry(mood, data_file)

        elif choice == '2':
            # Передаём путь явно
            show_stats(data_file)

        elif choice == '3':
            print("👋 До свидания!")
            break

        else:
            print("❌ Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
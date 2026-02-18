from mood_diary import add_entry, get_all_entries, validate_mood

def main():
    print("🌟 ДНЕВНИК НАСТРОЕНИЙ")
    print("=" * 50)

    while True:
        print("\nМеню:")
        print("1. Добавить запись")
        print("2. Показать статистику")
        print("3. Выход")

        choice = input("\nВыберите действие (1-3): ").strip()

        if choice == '1':

            #mood = input("Введите настроение (good/bad/neutral/excellent): ")
            add_entry(validate_mood())

        elif choice == '2':
            print(get_all_entries())

        elif choice == '3':
            print("👋 До свидания!")
            break

        else:
            print("❌ Некорректный выбор. Попробуйте снова❌")


if __name__ == "__main__":
    main()
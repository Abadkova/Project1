import json
import datetime
import os

# Функция для создания новой заметки
def create_note():
    """Создает новую заметку и добавляет ее в список."""
    note_id = generate_note_id()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    print("Заметка успешно создана!")

# Функция для генерации уникального ID заметки
def generate_note_id():
    """Генерирует уникальный ID для новой заметки."""
    if not notes:
        return 1
    else:
        return max([note["id"] for note in notes]) + 1

# Функция для сохранения заметок в файл
def save_notes():
    """Сохраняет список заметок в файл notes.json."""
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)
    print("Заметки успешно сохранены!")

# Функция для загрузки заметок из файла
def load_notes():
    """Загружает список заметок из файла notes.json."""
    global notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
    else:
        notes = []
    print("Заметки успешно загружены!")

# Функция для вывода списка заметок
def display_notes():
    """Выводит список всех заметок."""
    if not notes:
        print("Список заметок пуст.")
        return
    for i, note in enumerate(notes):
        print(f"{i + 1}. {note['title']} ({note['timestamp']})")

# Функция для редактирования заметки
def edit_note():
    """Редактирует существующую заметку."""
    display_notes()
    note_index = int(input("Введите номер заметки для редактирования: ")) - 1
    if 0 <= note_index < len(notes):
        note = notes[note_index]
        print(f"Текущий заголовок: {note['title']}")
        new_title = input("Введите новый заголовок (оставьте пустым, чтобы не менять): ")
        print(f"Текущий текст: {note['body']}")
        new_body = input("Введите новый текст (оставьте пустым, чтобы не менять): ")
        if new_title:
            note['title'] = new_title
        if new_body:
            note['body'] = new_body
        note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Заметка успешно отредактирована!")
    else:
        print("Неверный номер заметки.")

# Функция для удаления заметки
def delete_note():
    """Удаляет существующую заметку."""
    display_notes()
    note_index = int(input("Введите номер заметки для удаления: ")) - 1
    if 0 <= note_index < len(notes):
        del notes[note_index]
        print("Заметка успешно удалена!")
    else:
        print("Неверный номер заметки.")

# Функция для поиска заметок по дате
def search_notes_by_date():
    """Ищет заметки по заданной дате."""
    date_str = input("Введите дату в формате YYYY-MM-DD: ")
    found_notes = []
    for note in notes:
        if note['timestamp'].startswith(date_str):
            found_notes.append(note)
    if found_notes:
        print("Найденные заметки:")
        for i, note in enumerate(found_notes):
            print(f"{i + 1}. {note['title']} ({note['timestamp']})")
    else:
        print("Заметки по указанной дате не найдены.")

# Функция для вывода выбранной заметки
def view_note():
    """Выводит выбранную заметку на экран."""
    display_notes()
    note_index = int(input("Введите номер заметки для просмотра: ")) - 1
    if 0 <= note_index < len(notes):
        note = notes[note_index]
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата/Время: {note['timestamp']}")
    else:
        print("Неверный номер заметки.")

# Глобальный список заметок
notes = []

# Основной цикл программы
load_notes()
while True:
    print("\nМеню:")
    print("1. Создать заметку")
    print("2. Вывести список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Поиск заметок по дате")
    print("6. Просмотреть заметку")
    print("7. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        display_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        search_notes_by_date()
    elif choice == "6":
        view_note()
    elif choice == "7":
        save_notes()
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

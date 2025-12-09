import json
import os
import xml.etree.ElementTree as ET
from datetime import datetime

JSON_FILE = 'events.json'
XML_FILE = 'events.xml'

def load_events(format_choice):
    if format_choice == 'json':
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return []
    elif format_choice == 'xml':
        if os.path.exists(XML_FILE):
            tree = ET.parse(XML_FILE)
            root = tree.getroot()
            events = []
            for event_elem in root.findall('event'):
                event = {
                    "type": event_elem.find('type').text,
                    "date": event_elem.find('date').text,
                    "time": event_elem.find('time').text,
                    "duration": int(event_elem.find('duration').text),
                    "description": event_elem.find('description').text
                }
                events.append(event)
            return events
        else:
            return []
    else:
        return []

def save_events(events, format_choice):
    if format_choice == 'json':
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(events, f, ensure_ascii=False, indent=4)
    elif format_choice == 'xml':
        root = ET.Element('events')
        for event in events:
            event_elem = ET.SubElement(root, 'event')
            ET.SubElement(event_elem, 'type').text = event['type']
            ET.SubElement(event_elem, 'date').text = event['date']
            ET.SubElement(event_elem, 'time').text = event['time']
            ET.SubElement(event_elem, 'duration').text = str(event['duration'])
            ET.SubElement(event_elem, 'description').text = event['description']
        tree = ET.ElementTree(root)
        tree.write(XML_FILE, encoding='utf-8', xml_declaration=True)

def add_event(events):
    event_type = input("Введите тип события (встреча, звонок и т.п.): ")
    date_str = input("Введите дату (ГГГГ-ММ-ДД): ")
    time_str = input("Введите время начала (ЧЧ:ММ): ")
    try:
        duration = int(input("Введите продолжительность в минутах (минимум 15): "))
        if duration < 15:
            print("Длительность должна быть не менее 15 минут.")
            return
    except ValueError:
        print("Некорректное значение продолжительности.")
        return
    description = input("Описание (опционально): ")
    event = {
        "type": event_type,
        "date": date_str,
        "time": time_str,
        "duration": duration,
        "description": description
    }
    events.append(event)
    print("Событие добавлено.")

def view_events(events, only_future=False, filter_date=None):
    today_str = datetime.now().strftime('%Y-%m-%d')
    for idx, event in enumerate(events):
        if only_future:
            if event['date'] < today_str:
                continue
        if filter_date and event['date'] != filter_date:
            continue
        print(f"{idx + 1}. {event['type']} на {event['date']} в {event['time']}, длительность: {event['duration']} мин. Описание: {event['description']}")

def delete_event(events):
    view_events(events)
    try:
        idx = int(input("Введите номер события для удаления: ")) - 1
        if 0 <= idx < len(events):
            del events[idx]
            print("Событие удалено.")
        else:
            print("Некорректный номер.")
    except ValueError:
        print("Некорректный ввод.")

def edit_event(events):
    view_events(events)
    try:
        idx = int(input("Введите номер события для редактирования: ")) - 1
        if 0 <= idx < len(events):
            event = events[idx]
            print("Оставьте пустым, чтобы оставить без изменений.")
            new_type = input(f"Тип ({event['type']}): ") or event['type']
            new_date = input(f"Дата ({event['date']}): ") or event['date']
            new_time = input(f"Время ({event['time']}): ") or event['time']
            new_duration_str = input(f"Длительность ({event['duration']}): ")
            if new_duration_str:
                try:
                    new_duration = int(new_duration_str)
                    if new_duration < 15:
                        print("Длительность должна быть не менее 15 минут.")
                        return
                except ValueError:
                    print("Некорректное значение длительности.")
                    return
            else:
                new_duration = event['duration']
            new_description = input(f"Описание ({event['description']}): ") or event['description']
            events[idx] = {
                "type": new_type,
                "date": new_date,
                "time": new_time,
                "duration": new_duration,
                "description": new_description
            }
            print("Событие обновлено.")
        else:
            print("Некорректный номер.")
    except ValueError:
        print("Некорректный ввод.")

def main():
    format_choice = ''
    while format_choice not in ['json', 'xml']:
        format_choice = input("Выберите формат хранения данных ('json' или 'xml'): ").strip().lower()

    events = load_events(format_choice)

    while True:
        print("\n1. Добавить событие")
        print("2. Просмотреть все события")
        print("3. Просмотреть предстоящие события")
        print("4. Просмотреть события на конкретную дату")
        print("5. Редактировать событие")
        print("6. Удалить событие")
        print("7. Выйти и сохранить")
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            add_event(events)
        elif choice == '2':
            print("\nВсе события:")
            view_events(events)
        elif choice == '3':
            print("\nПредстоящие события (сегодня и дальше):")
            view_events(events, only_future=True)
        elif choice == '4':
            filter_date = input("Введите дату для просмотра (ГГГГ-ММ-ДД): ")
            print(f"\nСобытия на {filter_date}:")
            view_events(events, filter_date=filter_date)
        elif choice == '5':
            edit_event(events)
        elif choice == '6':
            delete_event(events)
        elif choice == '7':
            save_events(events, format_choice)
            print("Данные сохранены. Выход.")
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()
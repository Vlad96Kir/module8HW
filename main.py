from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    # Отримати поточну дату
    current_date = datetime.now().date()

    # Знайти перший день тижня (понеділок)
    start_date = current_date - timedelta(days=current_date.weekday())

    # Знайти кінцевий день тижня (неділя)
    end_date = start_date + timedelta(days=6)

    # Зміщення для привітань, якщо перший день тижня - неділя
    offset = timedelta(days=1) if start_date.weekday() == 6 else timedelta(days=0)

    # Створити словник для зберігання користувачів по днях тижня
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    # Проходження по користувачам і визначення днів народження на тижні
    for user in users:
        birthday = user["birthday"].date()

        # Визначення наступного дня народження, якщо припадає на вихідний
        if birthday.weekday() > 4:
            next_birthday = birthday + timedelta(days=(7 - birthday.weekday()) + offset.days)
        else:
            next_birthday = birthday

        # Перевірка, чи наступне день народження потрапляє в діапазон тижня
        if start_date <= next_birthday <= end_date:
            # Визначення дня тижня наступного дня народження
            day_of_week = next_birthday.strftime("%A")

            # Додавання користувача до відповідного списку за днем тижня
            birthdays_per_week[day_of_week].append(user["name"])

    # Виведення списку користувачів по днях тижня
    for day, users in birthdays_per_week.items():
        if users:
            print(f"{day}: {', '.join(users)}")


# Перевірка
users = [
    {"name": "Olexandr", "birthday": datetime(2023, 5, 27)},
    {"name": "Taras", "birthday": datetime(2023, 5, 28)},
    {"name": "Vasyl`", "birthday": datetime(2023, 5, 29)},
    {"name": "Olena", "birthday": datetime(2023, 5, 30)},
    {"name": "Volodymyr", "birthday": datetime(2023, 5, 31)},
    {"name": "David", "birthday": datetime(2023, 6, 1)},
    {"name": "Stephania", "birthday": datetime(2023, 6, 2)},
    {"name": "Ignat", "birthday": datetime(2023, 6, 3)}
]

get_birthdays_per_week(users)

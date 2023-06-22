from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {'name': 'Килим', 'birthday': datetime(1990, 6, 22)},
    {'name': 'Жак', 'birthday': '24.06.1999'},
    {'name': 'Влад', 'birthday': datetime(1988, 6, 23)},
    {'name': 'Ян', 'birthday': datetime(1992, 6, 24)},
    {'name': 'Борис', 'birthday': datetime(1990, 6, 25)},
    {'name': 'Марія', 'birthday': '26.06.1999'},
    {'name': 'Кароліна', 'birthday': datetime(1988, 6, 27)},
    {'name': 'Олена', 'birthday': datetime(1992, 6, 28)},
    {'name': 'Ніна', 'birthday': datetime(1988, 6, 29)},
    {'name': 'Володимир', 'birthday': datetime(1992, 6, 30)}
]


def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5 - current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()


def check_epl(list_of_emp: list) -> dict:
    result = defaultdict(list)
    current_year = datetime.now().year
    start, end = get_period()

    for user in list_of_emp:
        bd = user["birthday"].date() if isinstance(user["birthday"], datetime) else datetime.strptime(user["birthday"],
                                                                                                      "%d.%m.%Y").date()
        bd = bd.replace(year=current_year)

        if bd.weekday() in (5, 6):
                # Перевіряємо, якщо день народження випадає на вихідні, переносимо його на понеділок наступного тижня
            while bd.weekday() != 0:  # 0 означає понеділок
                bd += timedelta(days=1)

        if start <= bd <= end:
            result[bd].append(user["name"])

    return result


if __name__ == "__main__":
    ukranian_days = {
        0: 'Понеділок',
        1: 'Вівторок',
        2: 'Середа',
        3: 'Четвер',
        4: "П'ятниця",
        5: 'Субота',
        6: 'Неділя'
    }

    for key, value in check_epl(users).items():
        day_of_week = ukranian_days[key.weekday()]
        print(day_of_week, value)

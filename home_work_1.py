"""
Модуль бота-помічника v_1_1

Цей модуль містить простого консольного бота-помічника з базовою функціональністю.
"""
from datetime import datetime, timedelta
from collections import defaultdict
from typing import List, Dict

def get_birthdays_per_week(users: List[Dict[str, datetime]]) -> None:
    """
    Виводить імена користувачів, у яких найближчі дні народження протягом наступного тижня.

    :param users: Список користувачів з іменем та датою народження.
    :return: None
    """
    # Підготовка Даних
    birthdays_by_day = defaultdict(list)

    # Отримання Поточної Дати
    today = datetime.today().date()

    # Перебір Користувачів
    for user in users:
        # Конвертація Дати
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Оцінка Дати на Цей Рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Порівняння з Поточною Датою
        delta_days = (birthday_this_year - today).days

        # Визначення Дня Тижня
        if delta_days < 7:
            # Якщо вихідний, переносимо на понеділок
            birthday_day = (today + timedelta(days=delta_days)).strftime("%A")
            if birthday_day == "Saturday" or birthday_day == "Sunday":
                birthday_day = "Monday"
            birthdays_by_day[birthday_day].append(name)

    # Виведення Результату
    for day, names in birthdays_by_day.items():
        print(f"{day}: {', '.join(names)}")

# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)}
]

get_birthdays_per_week(users)